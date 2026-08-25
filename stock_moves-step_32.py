# === Stage 32: Добавь журнал действий пользователя ===
# Project: StockMoves
from datetime import datetime

class ActionLog:
    def __init__(self):
        self.entries = []

    def log(self, action_type, detail="", user="system"):
        entry = {
            "timestamp": datetime.now(),
            "action_type": action_type,
            "detail": detail,
            "user": user
        }
        self.entries.append(entry)
        return entry

    def get_log(self):
        return self.entries

    def clear_log(self):
        self.entries.clear()

    def __len__(self):
        return len(self.entries)
