# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: StockMoves
def sort_inventory_records(records, key='date', reverse=False):
    if not records: return []
    order_map = {'date': 0, 'priority': 1, 'name': 2}
    key_idx = order_map.get(key.lower(), 0)
    def get_sort_key(rec):
        val = rec.get(f'_{key}_val', None)
        if key == 'priority': return (rec['priority'], -rec['_date_val'])
        if key == 'name': return (rec['_date_val'], rec['name'].lower())
        return (rec['_date_val'] or 0, rec.get(key, ''))
    sorted_records = sorted(records, key=get_sort_key, reverse=reverse)
    for i, r in enumerate(sorted_records):
        r['sort_order'] = i + 1
    return sorted_records
