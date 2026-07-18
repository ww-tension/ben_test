# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: StockMoves
def add_reminders_to_stock_moves(stock_moves_data):
    """Adds a simple reminder system with due dates for stock moves."""
    def create_reminder(movement, days_before_due=30):
        if 'due_date' not in movement:
            movement['due_date'] = datetime.now() + timedelta(days=days_before_due)
            movement['reminder_sent'] = False
            print(f"Reminder created for stock move {movement.get('id', 'unknown')} due on {movement['due_date'].date()}")
        return movement

    def check_and_send_reminders(stock_moves_data, days_overdue_check=0):
        reminders = []
        now = datetime.now()
        for i, move in enumerate(stock_moves_data):
            if 'due_date' in move and not move.get('reminder_sent', False):
                due = datetime.strptime(move['due_date'], '%Y-%m-%d')
                if (now - due).days >= days_overdue_check:
                    move['reminder_sent'] = True
                    reminders.append(f"Stock move {move.get('id', 'unknown')} is overdue by {(now - due).days} days. Please process.")
        return reminders

    def add_due_date(stock_moves_data, date_str):
        for i, move in enumerate(stock_moves_data):
            if 'due_date' not in move:
                move['due_date'] = datetime.strptime(date_str, '%Y-%m-%d')
        return stock_moves_data

    def get_overdue_reminders(stock_moves_data, days_overdue=0):
        overdue = []
        now = datetime.now()
        for i, move in enumerate(stock_moves_data):
            if 'due_date' in move and not move.get('reminder_sent', False):
                due = datetime.strptime(move['due_date'], '%Y-%m-%d')
                if (now - due).days >= days_overdue:
                    overdue.append(move)
        return overdue

    def remove_expired_reminders(stock_moves_data):
        stock_moves_data[:] = [move for move in stock_moves_data if not move.get('reminder_sent', False)]
        return stock_moves_data

    add_due_date(stock_moves_data, "2024-12-31")
    reminders = check_and_send_reminders(stock_moves_data)
    overdue = get_overdue_reminders(stock_moves_data)
    for r in reminders:
        print(r)
    if overdue:
        print("Overdue movements:")
        for o in overdue:
            print(f"  - {o.get('id', 'unknown')}")
    stock_moves_data = remove_expired_reminders(stock_moves_data)
    return stock_moves_data

if __name__ == "__main__":
    sample_moves = [
        {'id': 1, 'type': 'receipt', 'quantity': 50},
        {'id': 2, 'type': 'issue', 'quantity': -30},
    ]
    result = add_reminders_to_stock_moves(sample_moves)
    print("Stock moves with reminders:", result)
