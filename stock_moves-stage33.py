# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: StockMoves
import json, os, hashlib

class StockMoves:
    def __init__(self, db_file="stock_moves.json"):
        self.db_file = db_file
        self.items = {}
        self.moves = []
        self.history = []
        if os.path.exists(db_file):
            with open(db_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.items = data.get('items', {})
                self.moves = data.get('moves', [])
                self.history = data.get('history', [])

    def _save(self):
        data = {'items': self.items, 'moves': self.moves, 'history': self.history}
        with open(self.db_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def get_item(self, item_id):
        return self.items.get(item_id)

    def add_item(self, name, unit, qty=0):
        item_id = hashlib.md5(f"{name}{unit}".encode()).hexdigest()[:8]
        self.items[item_id] = {'id': item_id, 'name': name, 'unit': unit, 'qty': qty}
        self.history.append({'action': 'add_item', 'item_id': item_id, 'data': {'name': name, 'unit': unit, 'qty': qty}})
        self._save()
        return item_id

    def get_moves(self):
        return self.moves

    def add_move(self, item_id, direction, qty, reason=''):
        item = self.items.get(item_id)
        if not item:
            raise ValueError(f"Item {item_id} not found")
        if direction == 'in':
            item['qty'] += qty
        elif direction == 'out':
            if item['qty'] < qty:
                raise ValueError(f"Insufficient stock: {item['qty']} < {qty}")
            item['qty'] -= qty
        elif direction == 'adjust':
            item['qty'] += qty
        elif direction == 'transfer':
            pass
        else:
            raise ValueError(f"Invalid direction: {direction}")

        move_id = hashlib.md5(f"{direction}{item_id}{qty}".encode()).hexdigest()[:8]
        move = {'id': move_id, 'item_id': item_id, 'direction': direction, 'qty': qty, 'reason': reason}
        self.moves.append(move)
        self.history.append({'action': 'add_move', 'item_id': item_id, 'data': move})
        self._save()
        return move_id

    def undo_last(self):
        if not self.history:
            return
        last = self.history[-1]
        if last['action'] == 'add_item':
            item_id = last['data']['item_id']
            item = self.items.get(item_id)
            if item:
                item['qty'] = 0
                del self.items[item_id]
        elif last['action'] == 'add_move':
            item_id = last['data']['item_id']
            item = self.items.get(item_id)
            if item:
                item['qty'] += last['data']['qty']
        self.history.pop()
        self._save()

    def show_report(self):
        report = []
        for item_id, item in self.items.items():
            moves = [m for m in self.moves if m['item_id'] == item_id]
            report.append({'item': item, 'moves': moves})
        return report
