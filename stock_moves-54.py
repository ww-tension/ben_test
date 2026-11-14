# === Stage 54: Добавь режим избранных записей и быстрый доступ к ним ===
# Project: StockMoves
import json, os
DATA = "stockmoves_data.json"

def load_data():
    if not os.path.exists(DATA):
        return {"favourites": []}
    with open(DATA, "r", encoding="utf-8") as f:
        return json.load(f)

def save_data(data):
    with open(DATA, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def toggle_favourite(record_id):
    data = load_data()
    favs = data.get("favourites", [])
    if record_id in favs:
        favs.remove(record_id)
    else:
        favs.append(record_id)
    data["favourites"] = favs
    save_data(data)
    return favs

def get_favourites():
    data = load_data()
    favs = data.get("favourites", [])
    if not favs:
        return []
    records = []
    for rid in favs:
        for rec in MOVEMENTS:
            if rec["id"] == rid:
                rec["is_favourite"] = True
                records.append(rec)
                break
    return records

def add_favourite_hotkey():
    print("Режим избранных:")
    favs = get_favourites()
    if not favs:
        print("  (пока нет избранных)")
    for rec in favs:
        star = "★" if rec.get("is_favourite") else "☆"
        print(f"  {star} {rec['id']} | {rec['type']} | {rec['date']} | {rec['description']} | {rec['qty']}")
    print("\nНажмите F5, чтобы вернуться к журналу.")
