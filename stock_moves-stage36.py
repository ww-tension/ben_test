# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: StockMoves
def repair_simple_issues(store):
    """Проверка целостности и ремонт простых проблем в журнале."""
    issues = []
    if not store:
        return issues

    # Проверка: все остатки неотрицательны
    for item_id, moves in store.items():
        current_balance = sum(m['qty'] for m in moves)
        if current_balance < 0:
            issues.append(f"Negative balance for {item_id}: {current_balance}")
            # Исправление: обнуляем баланс
            for move in moves:
                if move['qty'] < 0:
                    move['qty'] = 0

    # Проверка: типы полей корректны
    for item_id, moves in store.items():
        for i, move in enumerate(moves):
            if not isinstance(move.get('qty'), (int, float)):
                issues.append(f"Invalid qty type in {item_id} move {i}")
                move['qty'] = 0
            if not isinstance(move.get('ts'), (int, float)):
                issues.append(f"Invalid ts type in {item_id} move {i}")
                move['ts'] = 0

    return issues
