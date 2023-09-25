numbers,number = [int(num) for num in input().split()]

first_set = set()
second_set = set()

for num  in range(numbers):
    first_set.add(input())

for num in range(number):
    second_set.add(input())

print("\n".join(first_set.intersection(second_set)))