# === Stage 46: Добавь миграцию версии структуры данных ===
# Project: StockMoves
def migrate_version(self, current_schema: dict) -> dict:
        """Миграция структуры данных с сохранением истории версий."""
        if self._version not in current_schema:
            current_schema[self._version] = {"schema": self._schema, "timestamp": datetime.now().isoformat()}
        return current_schema
