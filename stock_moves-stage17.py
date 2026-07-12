# === Stage 17: Добавь группировку записей по категориям ===
# Project: StockMoves
class Category:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Category({self.name!r})"


def categorize_move(move):
    """Assign a category to each move based on its type."""
    if isinstance(move, StockIn):
        return "Stock In"
    elif isinstance(move, StockOut):
        return "Stock Out"
    elif isinstance(move, Adjustment):
        return "Adjustment"
    else:
        return "Unknown"


def group_moves_by_category(moves):
    """Group moves into categories and return a dict of category -> list of moves."""
    grouped = {}
    for move in moves:
        cat = categorize_move(move)
        if cat not in grouped:
            grouped[cat] = []
        grouped[cat].append(move)
    return grouped


def display_category_summary(grouped):
    """Pretty-print category summary."""
    print("=" * 50)
    print("SUMMARY BY CATEGORY")
    print("=" * 50)
    for cat, moves in grouped.items():
        print(f"\n[{cat}] — {len(moves)} entries:")
        for m in moves:
            print(f"  - {m}")


def add_category_support_to_stock_moves():
    """Add category grouping to StockMoves."""
    # Add Category class (already defined above)
    # Register it with the system so new StockIn/StockOut records can reference categories.

    def categorize_move(move):
        if isinstance(move, StockIn):
            return "Stock In"
        elif isinstance(move, StockOut):
            return "Stock Out"
        elif isinstance(move, Adjustment):
            return "Adjustment"
        else:
            return "Unknown"

    def group_moves_by_category(moves):
        grouped = {}
        for move in moves:
            cat = categorize_move(move)
            if cat not in grouped:
                grouped[cat] = []
            grouped[cat].append(move)
        return grouped

    def display_category_summary(grouped):
        print("=" * 50)
        print("SUMMARY BY CATEGORY")
        print("=" * 50)
        for cat, moves in grouped.items():
            print(f"\n[{cat}] — {len(moves)} entries:")
            for m in moves:
                print(f"  - {m}")

    return categorize_move, group_moves_by_category, display_category_summary


# Example usage (uncomment to test):
if __name__ == "__main__":
    # Sample data
    sample_moves = [
        StockIn(100, "Widget A", 5.0),
        StockOut(30, "Widget A", 5.0),
        Adjustment(-2, reason="Recalculation"),
        StockIn(40, "Gadget B", 10.0),
    ]

    categorize_move, group_moves_by_category, display_category_summary = add_category_support_to_stock_moves()
    grouped = group_moves_by_category(sample_moves)
    display_category_summary(grouped)
