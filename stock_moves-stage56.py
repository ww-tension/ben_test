# === Stage 56: Добавь массовое обновление выбранных записей ===
# Project: StockMoves
def bulk_update(selected_moves, field, values):
    for mv in selected_moves:
        setattr(mv, field, values.get(mv.id, values[0] if len(values) == 1 else None))
