# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: StockMoves
class InventoryFilter:
    def __init__(self, records):
        self.records = records
    
    def filter_by_status(self, status_list):
        return [r for r in self.records if r.get('status') in status_list]
    
    def filter_by_category(self, category):
        return [r for r in self.records if r.get('category') == category]
    
    def filter_by_tags(self, tags):
        return [r for r in self.records if any(tag in r.get('tags', []) for tag in tags)]
    
    def combine_filters(self, status=None, category=None, tags=None):
        result = self.records
        if status:
            result = self.filter_by_status(status)
        if category:
            result = self.filter_by_category(category)
        if tags:
            result = self.filter_by_tags(tags)
        return result
