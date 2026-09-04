# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: StockMoves
def test_edge_cases():
    """Тесты пограничных случаев и ошибок."""
    assert Inventory().get_stock("nonexistent") is None
    assert Inventory().get_stock("nonexistent", default=0) == 0

    inv = Inventory()
    inv.add_stock("A", 100, 10)
    inv.consume("A", 50)
    assert inv.get_stock("A") == 50

    inv.add_stock("B", 0, 5)
    assert inv.get_stock("B") == 0

    inv.add_stock("C", 10, 3)
    inv.consume("C", 11)
    assert inv.get_stock("C") == 0

    inv.add_stock("D", 5, 2)
    inv.consume("D", 5)
    inv.consume("D", 1)  # должен быть обработан как ошибка
    try:
        inv.consume("D", 1)
    except ValueError:
        pass
    else:
        assert False, "Ожидается ValueError при попытке потребления больше остатка"

    inv.add_stock("E", 100, 100)
    inv.consume("E", 100)
    assert inv.get_stock("E") == 0

    inv.add_stock("F", 50, 5)
    inv.add_stock("F", 30, 6)
    assert inv.get_stock("F") == 80

    inv.add_stock("G", 10, 10)
    inv.add_stock("G", 0, 10)
    assert inv.get_stock("G") == 10

    inv.add_stock("H", 10, 10)
    inv.consume("H", 10)
    inv.consume("H", 0)  # должен быть допустим
    assert inv.get_stock("H") == 0
