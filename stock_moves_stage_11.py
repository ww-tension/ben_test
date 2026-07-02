# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: StockMoves
import json, os

def save_inventory(data: dict) -> None:
    filename = "inventory.json"
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"[OK] Данные сохранены в {filename}")
    except Exception as e:
        print(f"[ERROR] Не удалось сохранить файл: {e}")

def load_inventory() -> dict | None:
    filename = "inventory.json"
    if not os.path.exists(filename):
        return {"products": [], "moves": []}
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        # Восстановление структуры, если файл был создан вручную или частично заполнен
        if not isinstance(data.get("products"), list):
            return {"products": [], "moves": []}
        if not isinstance(data.get("moves"), list):
            return {"products": [], "moves": []}
        return data
    except json.JSONDecodeError:
        print("[WARN] Файл inventory.json повреждён, создаётся новый.")
        return {"products": [], "moves": []}
