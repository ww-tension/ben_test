# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: StockMoves
def search_inventory(items, query):
    if not query: return items
    q = query.lower()
    results = [item for item in items 
               if any(q in str(getattr(item, field, '')).lower() for field in ['name', 'sku', 'category'])]
    return results
