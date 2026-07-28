# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: StockMoves
import random
def reset_demo_data():
    """Сбрасывает все таблицы к пустым состояниям."""
    tables = ['products', 'categories', 'warehouses', 'suppliers',
              'purchase_orders', 'purchase_order_items', 'inventory_movements',
              'adjustments', 'stock_levels']
    for t in tables:
        execute(f"DELETE FROM {t}")

def clear_cache():
    """Очищает кеш и сбрасывает демо-данные."""
    reset_demo_data()
    print("Состояние полностью сброшено.")

if __name__ == "__main__":
    clear_cache()
