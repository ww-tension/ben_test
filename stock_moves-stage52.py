# === Stage 52: Добавь экспорт краткого отчёта в текстовом формате ===
# Project: StockMoves
def export_summary(path, movements, batches):
    with open(path, 'w', encoding='utf-8') as f:
        f.write('Журнал движения запасов\n')
        f.write('=' * 60 + '\n')
        total_in = total_out = 0
        for m in movements:
            if m['type'] == 'приход':
                total_in += m['qty']
            elif m['type'] == 'расход':
                total_out += m['qty']
            f.write(f"#{m['id']} | {m['date']} | {m['type']:6} | {m['sku']} | {m['qty']} шт\n")
        f.write('=' * 60 + '\n')
        f.write(f"Всего приходов: {total_in} шт\n")
        f.write(f"Всего расходов: {total_out} шт\n")
        f.write('=' * 60 + '\n')
        f.write('Партии:\n')
        for b in batches:
            f.write(f"{b['id']} | {b['sku']} | {b['qty']} шт | {b['cost']} руб | остаток: {b['remaining']} шт\n")
        f.write('=' * 60 + '\n')
        f.write('Отчёт сформирован.\n')
    return path
