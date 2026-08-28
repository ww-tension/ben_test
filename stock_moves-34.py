# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: StockMoves
TEMPLATES = {
    "default": {"type": "default", "description": "Базовая запись"},
    "receipt": {"type": "receipt", "description": "Приход"},
    "issue": {"type": "issue", "description": "Расход"},
    "adjust": {"type": "adjust", "description": "Пересчет"},
}

def create_from_template(template_name, **kwargs):
    if template_name not in TEMPLATES:
        raise ValueError(f"Нет шаблона {template_name!r}. Доступные: {list(TEMPLATES)}")
    tmpl = TEMPLATES[template_name]
    record_type = tmpl["type"]
    if record_type not in RECORD_TYPES:
        raise ValueError(f"Тип {record_type!r} не поддерживается")
    record = RECORD_TYPES[record_type](**kwargs)
    record._template = template_name
    return record
