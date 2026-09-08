# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: StockMoves
import argparse


def main():
    parser = argparse.ArgumentParser(description="StockMoves CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    p_report = sub.add_parser("report", help="show inventory")
    p_report.add_argument("--as-of", type=str, default=None, help="date string")

    p_stock = sub.add_parser("stock", help="list stock")
    p_stock.add_argument("--as-of", type=str, default=None)

    p_move = sub.add_parser("move", help="add a move")
    p_move.add_argument("type", choices=["in", "out"])
    p_move.add_argument("--sku", required=True)
    p_move.add_argument("--qty", type=float, required=True)
    p_move.add_argument("--date", default=None)
    p_move.add_argument("--note", default="")

    args = parser.parse_args()

    if args.command == "report":
        if not args.as_of:
            print("Please specify --as-of date")
            return
        print(f"--- Stock as of {args.as_of} ---")
        for sku, qty in stock.items():
            print(f"{sku}: {qty:.2f}")

    elif args.command == "stock":
        if not args.as_of:
            print("Please specify --as-of date")
            return
        print(f"--- Stock as of {args.as_of} ---")
        for sku, qty in stock.items():
            print(f"{sku}: {qty:.2f}")

    elif args.command == "move":
        if args.type == "in":
            stock[args.sku] = stock.get(args.sku, 0) + args.qty
        else:
            stock[args.sku] = max(0, stock.get(args.sku, 0) - args.qty)
        print(f"Added {args.qty} of {args.sku} (note: {args.note})")
