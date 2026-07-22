# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: StockMoves
def print_stock_report(moves, initial_inventory=None):
    if not moves:
        return
    by_date = {}
    for m in moves:
        d = m['date']
        by_date.setdefault(d, []).append(m)
    lines = []
    lines.append(f"{'Дата':^12} {'Товар':^16} {'Приход':>8} {'Расход':>8} {'Остаток':>8}")
    for d in sorted(by_date):
        items = by_date[d]
        current_inv = dict(initial_inventory) if initial_inventory else {}
        for m in items:
            name = m['product']
            qty = m.get('quantity', 0)
            sign = 1 if m['type'] == 'in' else -1
            current_inv[name] = current_inv.get(name, 0) + sign * qty
        lines.append(f"{d:^12} {name:^16} {qty:>8} {'':>8} {current_inv.get(name, 0):>8}")
    print('\n'.join(lines))
