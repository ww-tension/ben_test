# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: StockMoves
import unittest

class TestStockMoves(unittest.TestCase):
    def test_add_and_decrease(self):
        from stockmoves import StockMoves
        sm = StockMoves()
        sm.add("Widget", 100, 10.0)
        sm.decrease("Widget", 20)
        self.assertEqual(sm.get_balance("Widget"), 80)

    def test_add_and_decrease_negative_balance(self):
        from stockmoves import StockMoves
        sm = StockMoves()
        sm.add("Widget", 10, 10.0)
        sm.decrease("Widget", 20)
        self.assertEqual(sm.get_balance("Widget"), -10)

    def test_decrease_without_add(self):
        from stockmoves import StockMoves
        sm = StockMoves()
        sm.decrease("Widget", 5)
        self.assertEqual(sm.get_balance("Widget"), -5)

    def test_get_balance_nonexistent(self):
        from stockmoves import StockMoves
        sm = StockMoves()
        self.assertIsNone(sm.get_balance("Widget"))

    def test_get_balance_zero(self):
        from stockmoves import StockMoves
        sm = StockMoves()
        sm.add("Widget", 10, 10.0)
        sm.decrease("Widget", 10)
        self.assertEqual(sm.get_balance("Widget"), 0)

    def test_get_balance_negative(self):
        from stockmoves import StockMoves
        sm = StockMoves()
        sm.add("Widget", 10, 10.0)
        sm.decrease("Widget", 20)
        self.assertEqual(sm.get_balance("Widget"), -10)

    def test_get_balance_large(self):
        from stockmoves import StockMoves
        sm = StockMoves()
        sm.add("Widget", 1000, 10.0)
        sm.decrease("Widget", 500)
        self.assertEqual(sm.get_balance("Widget"), 500)

    def test_get_balance_multiple_adds(self):
        from stockmoves import StockMoves
        sm = StockMoves()
        sm.add("Widget", 100, 10.0)
        sm.add("Widget", 200, 10.0)
        self.assertEqual(sm.get_balance("Widget"), 300)

    def test_get_balance_multiple_decreases(self):
        from stockmoves import StockMoves
        sm = StockMoves()
        sm.add("Widget", 100, 10.0)
        sm.decrease("Widget", 30)
        sm.decrease("Widget", 40)
        self.assertEqual(sm.get_balance("Widget"), 30)

    def test_get_balance_multiple_adds_and_decreases(self):
        from stockmoves import StockMoves
        sm = StockMoves()
        sm.add("Widget", 100, 10.0)
        sm.decrease("Widget", 30)
        sm.add("Widget", 50, 10.0)
        sm.decrease("Widget", 20)
        self.assertEqual(sm.get_balance("Widget"), 100)

    def test_get_balance_large_values(self):
        from stockmoves import StockMoves
        sm = StockMoves()
        sm.add("Widget", 1000000, 10.0)
        sm.decrease("Widget", 500000)
        self.assertEqual(sm.get_balance("Widget"), 500000)

    def test_get_balance_negative_values(self):
        from stockmoves import StockMoves
        sm = StockMoves()
        sm.add("Widget", -100, 10.0)
        sm.decrease("Widget", -50)
        self.assertEqual(sm.get_balance("Widget"), -150)

    def test_get_balance_zero_values(self):
        from stockmoves import StockMoves
        sm = StockMoves()
        sm.add("Widget", 0, 10.0)
        sm.decrease("Widget", 0)
        self.assertEqual(sm.get_balance("Widget"), 0)

    def test_get_balance_large_negative_values(self):
        from stockmoves import StockMoves
        sm = StockMoves()
        sm.add("Widget", -1000000, 10.0)
        sm.decrease("Widget", -500000)
        self.assertEqual(sm.get_balance("Widget"), -1500000)

    def test_get_balance_large_positive_values(self):
        from stockmoves import StockMoves
        sm = StockMoves()
        sm.add("Widget", 1000000, 10.0)
        sm.decrease("Widget", 500000)
        self.assertEqual(sm.get_balance("Widget"), 500000)

    def test_get_balance_large_negative_values(self):
        from stockmoves import StockMoves
        sm = StockMoves()
        sm.add("Widget", -1000000, 10.0)
        sm.decrease("Widget", -500000)
        self.assertEqual(sm.get_balance("Widget"), -1500000)

    def test_get_balance_zero_values(self):
        from stockmoves import StockMoves
        sm = StockMoves()
        sm.add("Widget", 0, 10.0)
        sm.decrease("Widget", 0)
        self.assertEqual(sm.get_balance("Widget"), 0)

if __name__ == "__main__":
    unittest.main()
