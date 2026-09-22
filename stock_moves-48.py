# === Stage 48: Проведи рефакторинг: разнеси крупные функции, сохрани совместимость публичных команд ===
# Project: StockMoves
def _split_move_into_receipts_and_consumption(move):
    """Разделяет одну запись движения на несколько записей прихода и расхода
    по каждой партии в рамках одной транзакции (приход/расход).
    
    Args:
        move: dict с полями _id, _type, _quantity, _cost, _ref, _date,
              _warehouse_id, _category_id, _supplier_id, _receiver_id.
    
    Returns:
        list[dict]: список записей, каждый из которых содержит _id, _type,
                     _quantity, _cost, _ref, _date и все остальные поля move.
    """
    move_id = move["_id"]
    move_type = move["_type"]
    date = move["_date"]
    warehouse_id = move["_warehouse_id"]
    category_id = move["_category_id"]
    supplier_id = move["_supplier_id"]
    receiver_id = move["_receiver_id"]
    ref = move["_ref"]
    cost = move["_cost"]
    quantity = move["_quantity"]
    unit_cost = cost / quantity if quantity else 0.0

    result = []
    if move_type == "receipt":
        for i in range(quantity):
            result.append({
                "_id": f"{move_id}-{i}-{move_type}",
                "_type": "receipt",
                "_quantity": 1,
                "_cost": unit_cost,
                "_ref": ref,
                "_date": date,
                "_warehouse_id": warehouse_id,
                "_category_id": category_id,
                "_supplier_id": supplier_id,
                "_receiver_id": receiver_id,
            })
    elif move_type == "consumption":
        for i in range(quantity):
            result.append({
                "_id": f"{move_id}-{i}-{move_type}",
                "_type": "consumption",
                "_quantity": 1,
                "_cost": unit_cost,
                "_ref": ref,
                "_date": date,
                "_warehouse_id": warehouse_id,
                "_category_id": category_id,
                "_supplier_id": supplier_id,
                "_receiver_id": receiver_id,
            })
    return result
