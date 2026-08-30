# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: StockMoves
def next_action(rec):
    """
    Рекомендация следующего действия на основе текущего состояния журнала.
    Возвращает строку с действием или None.
    """
    if not rec.get('moves'):
        return 'Добавьте первую запись прихода (приход товара).'
    last = rec['moves'][-1]
    if last.get('type') == 'arrival' and rec['arrivals'] == rec['moves']:
        return 'Добавьте расход (отгрузка товара из склада).'
    if last.get('type') == 'consumption' and rec['consumptions'] == rec['moves']:
        return 'Добавьте приход (закупка товара на склад).'
    if rec.get('balance') is not None and rec['balance'].get('quantity') == 0:
        return 'Добавьте приход (закупка товара, т.к. остаток равен 0).'
    return None
