# === Stage 51: Добавь журнал изменений данных с отметками времени ===
# Project: StockMoves
class ChangeLog:
    def __init__(self):
        self._log = []

    def add(self, action, record_id, detail="", ts=None):
        self._log.append({
            "time": ts or datetime.now().isoformat(timespec="seconds"),
            "action": action,
            "record_id": record_id,
            "detail": detail
        })

    def log(self, action, record_id, detail="", ts=None):
        self.add(action, record_id, detail, ts)

    def log_in(self, record_id, qty, ts=None):
        self.add("in", record_id, f"приход +{qty}", ts)

    def log_out(self, record_id, qty, ts=None):
        self.add("out", record_id, f"расход -{qty}", ts)

    def log_batch(self, record_id, batch_id, ts=None):
        self.add("batch", record_id, detail=batch_id, ts=ts)

    def log_change(self, record_id, field, old, new, ts=None):
        self.add("change", record_id, f"{field}: {old} -> {new}", ts)

    def log_delete(self, record_id, ts=None):
        self.add("delete", record_id, ts=ts)

    def tail(self, n=10):
        return self._log[-n:]

    def by_record(self, record_id):
        return [c for c in self._log if c["record_id"] == record_id]

    def by_action(self, action):
        return [c for c in self._log if c["action"] == action]

    def __len__(self):
        return len(self._log)

    def __str__(self):
        lines = [f"Журнал изменений ({len(self._log)} записей)"]
        for c in self._log[-20:]:
            lines.append(f"{c['time']} | {c['action']:6} | id={c['record_id']} | {c['detail']}")
        return "\n".join(lines)
