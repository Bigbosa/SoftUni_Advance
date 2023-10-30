from collections import deque

fuel_quantity = [int(el) for el in input().split(" ")]
add_fuel_quantity = deque(int(el) for el in input().split(" "))
necessary_fuel = deque(int(el) for el in input().split(" "))

length = len(fuel_quantity)

top_counter = 0

for i in range(length):
    current_fuel_quantity = fuel_quantity.pop()
    current_add_fuel_quantity = add_fuel_quantity.popleft()
    current_necessary_fuel = necessary_fuel.popleft()
    current_difference = current_fuel_quantity - current_add_fuel_quantity

    if current_difference < current_necessary_fuel:
        print(f"John did not reach: Altitude {top_counter + 1}")
        break
    else:
        top_counter += 1
        print(f"John has reached: Altitude {top_counter}")

if top_counter == length:
    print("John has reached all the altitudes and managed to reach the top!")

if top_counter == 0:
    print("John failed to reach the top.")
    print("John didn't reach any altitude.")






















