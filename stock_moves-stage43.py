# === Stage 43: Добавь пагинацию длинных списков ===
# Project: StockMoves
def paginate(records, page_size=20):
    total = len(records)
    pages = max(1, (total + page_size - 1) // page_size)
    for page in range(pages):
        start = page * page_size
        end = start + page_size
        if start >= total:
            break
        yield records[start:end], page, total, pages
