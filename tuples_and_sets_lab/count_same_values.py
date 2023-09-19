numbers_input = input().split()

result = {float(num): numbers_input.count(num) for num in numbers_input}
for number, counter in result.items():
    print(f"{number:.1f} - {counter} times")