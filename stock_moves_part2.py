# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: StockMoves
class StockValidationError(Exception): pass

def validate_quantity(value: str) -> int:
    if not value.strip(): raise StockValidationError("Количество пусто")
    try: return int(value)
    except ValueError: raise StockValidationError("Не числовое значение")

def validate_date(date_str: str) -> str:
    import datetime
    parts = date_str.split('-')
    if len(parts) != 3 or not all(p.isdigit() for p in parts):
        raise StockValidationError("Дата в формате ГГГГ-ММ-ДД")
    try: datetime.datetime(int(parts[0]), int(parts[1]), int(parts[2]))
    except ValueError: raise StockValidationError("Неверная дата")

def validate_sku(sku: str) -> str:
    if not sku or len(sku) > 50:
        raise StockValidationError("SKU должен быть от 1 до 50 символов")
    return sku.strip().upper()
