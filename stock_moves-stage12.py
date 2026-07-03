# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: StockMoves
def load_from_json(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if isinstance(data, list):
            for item in data:
                add_entry(item.get('date'), item.get('type'), item.get('product_id'), item.get('quantity'))
    except FileNotFoundError:
        print(f"Файл {filepath} не найден.")
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON в файле {filepath}: {e}")
    except KeyError as e:
        print(f"Неверная структура данных в файле {filepath}, пропущено поле: {e}")
