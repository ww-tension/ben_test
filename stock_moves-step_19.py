# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: StockMoves
def archive_old_records(db_path, cutoff_days=365):
    """Archive records older than cutoff_days into a separate file."""
    import sqlite3, os, datetime

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    try:
        table_name = cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name LIKE 'stock_moves%'").fetchone()[0]
    except Exception:
        print("[StockMoves] No stock_moves* table found.")
        return

    now = datetime.datetime.now().date()
    cutoff_date = (now - datetime.timedelta(days=cutoff_days)).isoformat()

    archived_path = db_path.replace('.db', '_archive.db') if '.db' in db_path else db_path + '_archive.sqlite3'

    old_records = cur.execute(f"SELECT * FROM {table_name} WHERE date <= ?", (cutoff_date,)).fetchall()
    conn.close()

    if not old_records:
        print("[StockMoves] No records to archive.")
        return

    conn_archive = sqlite3.connect(archived_path)
    cur_archive = conn_archive.cursor()

    # Create same schema in archive DB from the original
    try:
        table_name_orig = cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name LIKE 'stock_moves%'").fetchone()[0]
    except Exception:
        print("[StockMoves] Cannot determine original table name.")
        conn_archive.close()
        return

    schema = cur.execute(f"PRAGMA table_info({table_name_orig})").fetchall()
    columns = [col[1] for col in schema]
    create_sql = f'CREATE TABLE {table_name}_archive ({", ".join(columns)})'
    cur_archive.execute(create_sql)

    for row in old_records:
        cols = ', '.join(f'?' * len(row))
        placeholders = ', '.join(['?'] * len(row))
        try:
            cur_archive.execute(f"INSERT INTO {table_name}_archive VALUES ({placeholders})", row)
        except Exception as e:
            print(f"[StockMoves] Archive insert error: {e}")

    conn_archive.commit()
    conn_archive.close()

    # Remove old records from original DB
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    try:
        table_name = cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name LIKE 'stock_moves%'").fetchone()[0]
    except Exception:
        print("[StockMoves] Cannot determine original table name for cleanup.")
        return

    deleted_count = cur.execute(f"DELETE FROM {table_name} WHERE date <= ?", (cutoff_date,)).rowcount
    conn.commit()
    conn.close()

    print(f"[StockMoves] Archived {len(old_records)} records to {archived_path}; removed {deleted_count} from original.")
