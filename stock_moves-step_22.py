# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: StockMoves
def check_expired_reminders():
    """Проверяет просроченные напоминания и формирует список для вывода."""
    expired = []
    for item in inventory:
        if item.get("remind_date"):
            remind_str = item["remind_date"].replace("/", "-")
            try:
                remind_dt = datetime.strptime(remind_str, "%Y-%m-%d").date()
            except ValueError:
                continue
            if remind_dt < today:
                expired.append({
                    "name": item.get("product_name", item["id"]),
                    "quantity": item["total_qty"],
                    "unit_price": item.get("avg_cost"),
                    "remind_date": remind_str,
                })
    return expired
