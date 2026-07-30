# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: StockMoves
def compute_metrics(moves: list[dict], initial_stock: int) -> dict:
    stock = initial_stock
    metrics = {
        "total_in": 0,
        "total_out": 0,
        "net_change": 0,
        "final_stock": initial_stock,
        "turnover_ratio": 0.0,
    }
    for m in moves:
        if m["type"] == "in":
            metrics["total_in"] += m["qty"]
            stock += m["qty"]
        elif m["type"] == "out":
            metrics["total_out"] += m["qty"]
            stock -= m["qty"]
    metrics["net_change"] = metrics["total_in"] - metrics["total_out"]
    metrics["final_stock"] = stock
    total_moves = len(moves)
    if total_moves > 0:
        metrics["turnover_ratio"] = (
            (metrics["total_in"] + metrics["total_out"]) / total_moves
        )
    return metrics


def print_report(moves: list[dict], initial_stock: int) -> None:
    m = compute_metrics(moves, initial_stock)
    print(f"=== StockMoves Report ===")
    print(f"Incoming:   {m['total_in']} units")
    print(f"Outgoing:    {m['total_out']} units")
    print(f"Net change:  +{m['net_change']} units")
    print(f"Final stock: {m['final_stock']} units")
