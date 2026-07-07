# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: StockMoves
def print_stock_summary(store):
    """Generate a concise summary of the current inventory state."""
    total_items = len(store['items'])
    total_inbound = sum(move['qty'] for move in store['inbound_moves'])
    total_outbound = -sum(move['qty'] for move in store['outbound_moves'])

    print(f"=== Stock Summary ===")
    print(f"Total distinct items: {total_items}")
    print(f"Total inbound quantity: {total_inbound}")
    print(f"Total outbound quantity: {total_outbound}")

    if total_items > 0:
        current_stock = {}
        for item_name, qty in store['items'].items():
            current_stock[item_name] = qty
        sorted_items = sorted(current_stock.items(), key=lambda x: -x[1])
        print(f"\nCurrent stock levels:")
        for name, qty in sorted_items:
            status = "OK" if qty > 0 else "⚠️ LOW/OUT"
            print(f"  {name}: {qty} [{status}]")

    total_moves = len(store['inbound_moves']) + len(store['outbound_moves'])
    print(f"\nTotal moves recorded: {total_moves}")
