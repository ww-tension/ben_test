# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: StockMoves
def validate_date(date_str):
    """Validates date string in YYYY-MM-DD format and returns a tuple of (year, month, day) or raises ValueError."""
    if not isinstance(date_str, str) or len(date_str) != 10:
        raise ValueError(f"Invalid date format: {date_str!r} — expected YYYY-MM-DD")
    parts = date_str.split('-')
    try:
        year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
    except ValueError:
        raise ValueError(f"Invalid date format: {date_str!r} — non-numeric characters detected")

    if not (1 <= month <= 12):
        raise ValueError(f"Invalid month in date: {date_str!r}")
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days_in_month[2] = 29
    if not (1 <= day <= days_in_month[month]):
        raise ValueError(f"Invalid day in date: {date_str!r}")

    return year, month, day
