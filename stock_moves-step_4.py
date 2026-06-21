# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: StockMoves
def edit_record(record_id, updates):
    if record_id not in inventory_records:
        print(f"Запись с ID {record_id} не найдена.")
        return False
    
    for key, value in updates.items():
        if key in ['id', 'created_at']:
            continue
        inventory_records[record_id][key] = value
    
    # Сохранение в файл (предполагается наличие функции save_to_file)
    try:
        save_to_file()
        print(f"Запись {record_id} успешно обновлена.")
        return True
    except Exception as e:
        print(f"Ошибка при сохранении: {e}")
        return False
