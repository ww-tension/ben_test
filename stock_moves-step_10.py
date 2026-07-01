# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: StockMoves
def export_to_json():
    import json
    from datetime import datetime
    data = {
        "timestamp": datetime.utcnow().isoformat(),
        "inventory_items": inventory.items,
        "transactions": transactions,
        "summary": calculate_summary()
    }
    return json.dumps(data, indent=2, ensure_ascii=False)
