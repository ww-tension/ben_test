# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: StockMoves
def monthly_stats(records, period='month'):
    """Return aggregated stats grouped by date (day/month/year)."""
    from collections import defaultdict

    groups = defaultdict(lambda: {'in': 0, 'out': 0, 'balance': 0})
    for rec in records:
        key = rec['date']
        if period == 'month':
            key = key[:7]  # YYYY-MM
        elif period == 'year':
            key = key[:4]
        groups[key]['in'] += rec.get('qty', 0)
        groups[key]['out'] -= rec.get('qty', 0)
    return dict(sorted(groups.items()))
