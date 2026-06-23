# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: StockMoves
def remove_record(record_id: int) -> bool:
    """Удаление записи по ID с обработкой отсутствия."""
    if record_id not in inventory_moves:
        print(f"Ошибка: запись с ID {record_id} не найдена.")
        return False
    
    del inventory_moves[record_id]
    
    # Пересчет остатков после удаления
    recalculate_balances()
    
    print(f"Запись с ID {record_id} успешно удалена.")
    return True

# Пример вызова (раскомментируйте для тестирования):
# remove_record(10)
