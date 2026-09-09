# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: StockMoves
import copy

def dry_run(operation, record):
    """Simulate an inventory operation without persisting data.
    Returns the simulated state changes.
    """
    if operation in ("IN", "OUT"):
        qty = record.get("qty", 0)
        if not qty:
            return {"error": f"Invalid {operation}: qty must be > 0"}
        return {"status": "dry-run", "operation": operation, "qty": qty, "note": "no persistence"}
    elif operation == "COST":
        price = record.get("price", 0)
        if not price:
            return {"error": "Invalid COST: price must be > 0"}
        return {"status": "dry-run", "operation": "COST", "price": price, "note": "no persistence"}
    elif operation == "MOVE":
        qty = record.get("qty", 0)
        if not qty:
            return {"error": "Invalid MOVE: qty must be > 0"}
        return {"status": "dry-run", "operation": "MOVE", "qty": qty, "note": "no persistence"}
    else:
        return {"error": f"Unknown operation: {operation}"}
