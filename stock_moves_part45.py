# === Stage 45: Добавь восстановление из резервной копии ===
# Project: StockMoves
import json, os

def restore_from_backup(backup_path, data_path):
    if not os.path.exists(backup_path):
        print(f"Резервная копия не найдена: {backup_path}")
        return False
    try:
        with open(backup_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        with open(data_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Резервная копия успешно восстановлена из {backup_path}")
        return True
    except Exception as e:
        print(f"Ошибка восстановления: {e}")
        return False
