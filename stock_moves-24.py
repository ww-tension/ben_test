# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: StockMoves
def print_move_detail(move):
    print(f"Move #{move.id}")
    print(f"  Type: {move.type_name}")
    print(f"  Date: {move.date.strftime('%Y-%m-%d') if move.date else 'N/A'}")
    if hasattr(move, 'product'):
        print(f"  Product: {move.product.name or move.product_id}")
    if hasattr(move, 'quantity'):
        print(f"  Qty: {move.quantity} (direction: {'+' if move.direction == 'in' else '-'}{abs(move.quantity)})")
    if hasattr(move, 'unit_price') and move.unit_price is not None:
        print(f"  Price: {move.unit_price}")
    if hasattr(move, 'reference'):
        print(f"  Ref: {move.reference}")
