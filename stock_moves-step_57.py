# === Stage 57: Добавь массовое удаление с подтверждением через параметр ===
# Project: StockMoves
def mass_delete(moves, ids, confirm=True):
    target = {int(i) for i in ids}
    if confirm:
        n = len(target)
        print(f"Удалить {n} записей из журнала? (y/n) ", end="")
        ans = input().strip().lower()
        if ans != "y":
            print("Отмена.")
            return
    removed = []
    for m in moves:
        if m["id"] in target:
            removed.append(m)
    for m in removed:
        moves.remove(m)
    print(f"Удалено записей: {len(removed)}")
    return removed
