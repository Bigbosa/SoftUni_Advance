main_string = input()

result = {}

for symbols in main_string:
    result[symbols] = f": {main_string.count(symbols)} time/s"

for sym, rep in sorted(result.items()):
    print(f"{sym}{rep}")

