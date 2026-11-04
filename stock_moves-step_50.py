# === Stage 50: Сделай аккуратную финальную полировку сообщений, названий функций и комментариев ===
# Project: StockMoves
def _format_quantity(value):
    if isinstance(value, float) and value.is_integer():
        return f"{int(value)} шт."
    return f"{value:.2f} шт."


def _format_money(value):
    return f"{value:,.2f} ₽"


def _format_date(date_value):
    if isinstance(date_value, str):
        return date_value
    return date_value.strftime("%d.%m.%Y")


def _format_reference(ref_value):
    if not ref_value:
        return "—"
    return str(ref_value)


def _format_line(line):
    document = _format_reference(line.get("document"))
    date = _format_date(line.get("date"))
    product = line.get("product", {}).get("name", "—")
    movement = line.get("movement", "—")
    quantity = _format_quantity(line.get("quantity", 0))
    return (
        f"[{document}] {date} | {movement:<6} | "
        f"{quantity:<10} | {product}"
    )


def _format_document(document):
    reference = _format_reference(document.get("reference"))
    date = _format_date(document.get("date"))
    title = document.get("title", "Движение")
    return f"[{reference}] {date} | {title}"


def _format_inventory(inventory):
    product = inventory.get("product", {}).get("name", "—")
    quantity = _format_quantity(inventory.get("quantity", 0))
    cost = _format_money(inventory.get("cost", 0))
    return f"{product:<20} {quantity:<10} {cost}"


def _format_summary(summary):
    if not summary:
        return "Нет данных за выбранный период."
    lines = [
        f"Записей: {summary.get('count', 0)}",
        f"Приход: {_format_quantity(summary.get('income', 0))}",
        f"Расход: {_format_quantity(summary.get('expense', 0))}",
        f"Остаток: {_format_quantity(summary.get('balance', 0))}",
    ]
    return "\n".join(lines)
