# === Stage 47: Добавь финальную функцию demo(), которая показывает основной пользовательский сценарий ===
# Project: StockMoves
def demo():
    print("=" * 60)
    print("DEMO: StockMoves — Журнал движения запасов")
    print("=" * 60)

    # Создание товара
    product = StockProduct("Винный шкаф", "Шкафы")
    product.set_price(3500)
    print(f"Товар: {product}")

    # Приход
    receipt = StockReceipt("Приход", "001", product, 15)
    receipt.set_price(3500)
    receipt.set_supplier("ООО ВиноТорг")
    receipt.set_date("2024-03-01")
    receipt.register()
    print(f"Приход: {receipt}")

    # Расход
    issue = StockIssue("Расход", "002", product, 12)
    issue.set_price(3500)
    issue.set_customer("Салон Реновация")
    issue.set_date("2024-03-05")
    issue.register()
    print(f"Расход: {issue}")

    # Проверка остатка
    print(f"\nОстаток: {product.get_stock()} шт.")

    # Попытка расхода больше остатка
    try:
        bad_issue = StockIssue("Расход", "003", product, 5)
        bad_issue.set_price(3500)
        bad_issue.set_customer("Тест")
        bad_issue.set_date("2024-03-10")
        bad_issue.register()
    except ValueError as e:
        print(f"Ошибка: {e}")

    print("\nДемо завершена.")
