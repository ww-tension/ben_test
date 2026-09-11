# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: StockMoves
import sys

ANSI = sys.stdout.isatty()

def c(color, text):
    if ANSI:
        codes = {
            'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m',
            'blue': '\033[34m', 'magenta': '\033[35m', 'cyan': '\033[36m',
            'white': '\033[37m', 'bold': '\033[1m', 'reset': '\033[0m'
        }
        return codes.get(color, '') + text + codes['reset']
    return text

def print_move(move):
    date = c('bold', move['date'] or '')
    action = c('green', '+') if move['direction'] == 'in' else c('red', '-')
    qty = c('cyan', f' {move["quantity"]} шт')
    print(f'{date} | {action} {move["direction"]} | {move["product"]} {qty}')
