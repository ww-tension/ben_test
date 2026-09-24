# === Stage 49: Добавь финальную самопроверку приложения и отчёт о готовности ===
# Project: StockMoves
def self_check_and_report():
    """Compact final self-check: verify core classes exist and run a demo transaction."""
    from stockmoves.app import App

    app = App()

    # --- 1. Basic sanity: can we create an item and log a receipt? ---
    item = app.create_item("Widget", sku="W01", uom="pcs", cost=10.0)
    assert item.name == "Widget"

    receipt = app.create_receipt(item, qty=5, price=10.0)
    assert receipt.qty == 5
    assert receipt.total == 50.0

    # --- 2. Check that the journal records the move ---
    moves = app.get_moves()
    assert len(moves) == 1
    assert moves[0].type == "IN"
    assert moves[0].qty == 5

    # --- 3. Check that stock balance is correct ---
    balance = app.get_stock_balance(item)
    assert balance.qty == 5
    assert balance.total_cost == 50.0

    # --- 4. Add a second item and a mixed journal ---
    item2 = app.create_item("Gadget", sku="G02", uom="pcs", cost=25.0)
    app.create_receipt(item2, qty=10, price=25.0)
    app.create_issue(item2, qty=3, price=25.0)

    moves2 = app.get_moves()
    assert len(moves2) == 3

    balances = app.get_stock_balances()
    assert len(balances) == 2

    # --- 5. Final report ---
    print("=" * 50)
    print("StockMoves — Final Self-Check Report")
    print("=" * 50)
    print(f"Total moves recorded: {len(moves2)}")
    print(f"Total stock items: {len(balances)}")
    print(f"Widget balance: qty={balance.qty}, value={balance.total_cost}")
    gadget = app.get_stock_balance(item2)
    print(f"Gadget balance: qty={gadget.qty}, value={gadget.total_cost}")
    print(f"Total stock value: {balance.total_cost + gadget.total_cost}")
    print("=" * 50)
    print("All checks passed. Project is ready for use.")
    print("=" * 50)

if __name__ == "__main__":
    self_check_and_report()
