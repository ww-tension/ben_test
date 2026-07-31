# === Stage 29: Добавь конфигурацию приложения через словарь настроек ===
# Project: StockMoves
def get_settings():
    """Возвращает словарь конфигурации приложения."""
    return {
        "app_name": "StockMoves",
        "version": 29,
        "default_currency": "RUB",
        "log_file": "stock_moves.log",
        "show_qty_zero_threshold": 5,
        "report_date_format": "%Y-%m-%d",
    }
