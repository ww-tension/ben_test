# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: StockMoves
def backup_data_file(data_path, backup_dir=None):
    """Создаёт резервную копию файла данных с timestamp."""
    import os
    if not os.path.exists(data_path):
        print(f"Файл данных не найден: {data_path}")
        return None
    if backup_dir is None:
        backup_dir = os.path.join(os.path.dirname(data_path), "backups")
    os.makedirs(backup_dir, exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, f"backup_{os.path.basename(data_path)}_{timestamp}")
    shutil.copy2(data_path, backup_path)
    print(f"Резервная копия сохранена: {backup_path}")
    return backup_path
