number_of_elements = int(input())

elements = set()

for _ in range(number_of_elements):
    how_many_elements = input().split()
    for element in how_many_elements:
        elements.add(element)

print("\n".join(elements))
