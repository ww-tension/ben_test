# === Stage 53: Добавь импорт отчёта или списка записей из простого текстового формата ===
# Project: StockMoves
def import_text_file(path, sep="\t"):
    records = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(sep)
                if len(parts) < 5:
                    continue
                rec = {
                    "date": parts[0].strip(),
                    "type": parts[1].strip().lower(),
                    "item": parts[2].strip(),
                    "qty": float(parts[3]),
                    "note": parts[4].strip(),
                }
                records.append(rec)
    except FileNotFoundError:
        print(f"Файл не найден: {path}")
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
    return records

def export_text_file(records, path, sep="\t"):
    try:
        with open(path, "w", encoding="utf-8") as f:
            for r in records:
                f.write(sep.join([
                    r.get("date", ""),
                    r.get("type", ""),
                    r.get("item", ""),
                    str(r.get("qty", "")),
                    r.get("note", ""),
                ]) + "\n")
    except Exception as e:
        print(f"Ошибка при записи файла: {e}")
