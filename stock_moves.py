# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: StockMoves
import json, uuid
from datetime import date

class StockMove:
    def __init__(self):
        self.items = {}
        self.moves = []
    
    def add_item(self, name, initial_qty=0):
        if name not in self.items:
            self.items[name] = {'name': name, 'qty': 0}
        return self
    
    def receive(self, item_name, qty, batch_id=None):
        if batch_id is None: batch_id = str(uuid.uuid4())[:8]
        date_str = date.today().isoformat()
        move = {'type': 'IN', 'item': item_name, 'qty': qty, 'batch': batch_id, 'date': date_str}
        self.moves.append(move)
        if item_name in self.items:
            self.items[item_name]['qty'] += qty
        return move
    
    def consume(self, item_name, qty):
        if item_name not in self.items or self.items[item_name]['qty'] < qty:
            raise ValueError("Недостаточно товара")
        date_str = date.today().isoformat()
        move = {'type': 'OUT', 'item': item_name, 'qty': qty, 'date': date_str}
        self.moves.append(move)
        self.items[item_name]['qty'] -= qty
        return move
    
    def get_report(self):
        report = []
        for m in sorted(self.moves, key=lambda x: x['date']):
            item = self.items.get(m['item'], {})
            report.append(f"{m['type']:4} | {m['item']:10} | {m['qty']:+6} | Остаток: {self.items[m['item']]['qty']}")
        return "\n".join(report)

if __name__ == "__main__":
    app = StockMove()
    app.add_item("Винт М4").add_item("Гайка М4", 50).receive("Винт М4", 100, "BATCH-01") \
         .consume("Винт М4", 20) \
         .receive("Гайка М4", 80) \
         .consume("Гайка М4", 5).get_report()
