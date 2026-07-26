# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: StockMoves
def demo_stock_moves():
    print("=== DEMO: StockMoves Manual Test ===")
    moves = []
    
    # 1. Товар "Яблоки" — приход
    moves.append({"type": "incoming", "product": "Яблоки", "qty": 50, "date": "2024-06-01"})
    print(f"[1] Приход: Яблоки +50 шт ({moves[-1]['date']})")

    # 2. Расход — продажа
    moves.append({"type": "outgoing", "product": "Яблоки", "qty": 30, "date": "2024-06-02"})
    print(f"[2] Расход: Яблоки -30 шт ({moves[-1]['date']})")

    # 3. Остаток
    balance = sum(m['qty'] if m['type']=='incoming' else -m['qty'] for m in moves)
    print(f"\n[3] Текущий остаток Яблок: {balance} шт.")

    # 4. Добавим "Молоко" — партия с пересортицой
    moves.append({"type": "incoming", "product": "Молоко", "qty": 10, "date": "2024-06-03"})
    print(f"[4] Приход: Молоко +10 шт ({moves[-1]['date']})")

    moves.append({"type": "outgoing", "product": "Молоко", "qty": 8, "date": "2024-06-03"})
    print(f"[5] Расход: Молоко -8 шт ({moves[-1]['date']})")

    balance_milk = sum(m['qty'] if m['type']=='incoming' else -m['qty'] for m in moves if m['product']=='Молоко')
    print(f"\n[6] Остаток Молока: {balance_milk} шт.")

    # 5. Пересортица — приход больше расхода
    moves.append({"type": "incoming", "product": "Яблоки", "qty": 20, "date": "2024-06-05"})
    print(f"[7] Приход: Яблоки +20 шт ({moves[-1]['date']})")

    balance_apple = sum(m['qty'] if m['type']=='incoming' else -m['qty'] for m in moves if m['product']=='Яблоки')
    print(f"\n[8] Итого яблок: {balance_apple} шт.")

    # 6. Сводка по всем товарам
    all_products = {}
    for m in moves:
        p = m['product']
        if p not in all_products:
            all_products[p] = []
        all_products[p].append(m)

    print("\n=== ИТОГО ===")
    for prod, plist in all_products.items():
        total = sum(x['qty'] if x['type']=='incoming' else -x['qty'] for x in plist)
        print(f"  {prod}: {total} шт.")

    print("=== DEMO COMPLETE ===")
    
    return moves
