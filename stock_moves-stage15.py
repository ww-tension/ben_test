# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: StockMoves
def weekly_stats(moves: list[dict]) -> dict[str, dict]:
    """Weekly stock movement statistics grouped by date (ISO week)."""
    from datetime import date, timedelta, datetime
    weeks = {}
    for m in moves:
        if "date" not in m or m["date"] is None:
            continue
        try:
            d = datetime.strptime(m["date"], "%Y-%m-%d").date()
        except ValueError:
            continue
        week_id = (d - date(d.year, 1, 1)).isocalendar()[1]
        key = f"W{week_id}"
        weeks.setdefault(key, {"in": 0, "out": 0})
        weeks[key]["in"] += m.get("qty", 0)
        weeks[key]["out"] -= m.get("qty", 0)
    return {k: dict(v) for k, v in sorted(weeks.items())}
