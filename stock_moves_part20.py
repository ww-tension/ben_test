# === Stage 20: Добавь восстановление записей из архива ===
# Project: StockMoves
def restore_from_archive(archive_path, main_db):
    """Восстанавливает записи из резервной копии в основную базу данных."""
    try:
        with open(archive_path, 'r', encoding='utf-8') as f:
            lines = [l.strip() for l in f.readlines() if l.strip()]

    except FileNotFoundError:
        print(f"Файл архива не найден: {archive_path}")
        return 0

    count = 0
    for line in lines:
        parts = line.split('|')
        if len(parts) == 6:
            try:
                id_, date, type_, product_id, quantity, note = parts
                main_db.append({
                    'id': int(id_),
                    'date': date.strip(),
                    'type': type_.strip(),
                    'product_id': int(product_id),
                    'quantity': float(quantity) if '.' in quantity else int(quantity),
                    'note': note.strip()
                })
                count += 1

            except ValueError:
                print(f"Ошибка парсинга строки: {line}")

    print(f"Восстановлено записей: {count}")
    return count
