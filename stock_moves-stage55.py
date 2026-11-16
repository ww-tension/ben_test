# === Stage 55: Добавь мягкую проверку дубликатов при создании записей ===
# Project: StockMoves
def find_duplicate_moves(moves, new_move):
    for move in moves:
        if (move["product_id"] == new_move["product_id"] and
                move["date"] == new_move["date"] and
                move["type"] == new_move["type"] and
                move["batch_id"] == new_move.get("batch_id") and
                move["quantity"] == new_move["quantity"]):
            return True
    return False
