# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: StockMoves
class StockJournal:
    def __init__(self):
        self._records = []

    def add_inbound(self, product_id, qty, batch_no=None, note=""):
        record = {"type": "IN", "product_id": product_id, "qty": qty, "batch_no": batch_no or None, "note": note}
        self._records.append(record)
        return record

    def add_outbound(self, product_id, qty, batch_no=None, note=""):
        if not batch_no:
            raise ValueError("Batch number required for outbound")
        record = {"type": "OUT", "product_id": product_id, "qty": qty, "batch_no": batch_no, "note": note}
        self._records.append(record)
        return record

    def get_balance(self, product_id):
        total_qty = 0
        current_batch_qty = {}
        for rec in self._records:
            if rec["product_id"] != product_id:
                continue
            if rec["type"] == "IN":
                batch_key = rec.get("batch_no") or f"all_{rec['qty']}"
                total_qty += rec["qty"]
                current_batch_qty[batch_key] = current_batch_qty.get(batch_key, 0) + rec["qty"]
            elif rec["type"] == "OUT":
                batch_key = rec["batch_no"]
                if batch_key in current_batch_qty:
                    current_batch_qty[batch_key] -= rec["qty"]
                    if current_batch_qty[batch_key] <= 0:
                        del current_batch_qty[batch_key]
        return total_qty, dict(current_batch_qty)

    def get_history(self):
        return list(reversed(self._records))
