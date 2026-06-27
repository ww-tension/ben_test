# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: StockMoves
def print_menu():
    print("\n=== Меню StockMoves ===")
    print("1. Показать список товаров")
    print("2. Добавить приход товара")
    print("3. Оформить расход товара")
    print("4. Вывести журнал движений")
    print("5. Вывести текущие остатки")
    print("6. Сохранить и выйти")
    return input("Выберите действие (1-6): ")

def run_cli():
    while True:
        choice = print_menu()
        if choice == '1':
            for item in inventory.items():
                print(f"{item[0]}: {item[1]['name']} | Остаток: {sum(p['qty'] for p in item[2])} шт.")
        elif choice == '2':
            add_incoming()
        elif choice == '3':
            add_outgoing()
        elif choice == '4':
            print_journal()
        elif choice == '5':
            show_balance()
        elif choice == '6':
            save_data()
            break
