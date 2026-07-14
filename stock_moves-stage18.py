# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: StockMoves
import json, os

# --- StockMoves Inventory System v18: Tags support ---

class TagManager:
    """Manage product tags (add/remove)."""
    
    def __init__(self):
        self.tags = {}  # {tag_name: count}
        
    def add_tag(self, tag_name, quantity=0):
        if tag_name in self.tags:
            self.tags[tag_name] += quantity
        else:
            self.tags[tag_name] = quantity
            
    def remove_tag(self, tag_name, quantity=0):
        if tag_name in self.tags:
            self.tags[tag_name] -= quantity
            if self.tags[tag_name] <= 0:
                del self.tags[tag_name]
