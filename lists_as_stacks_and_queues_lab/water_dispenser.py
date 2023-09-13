from collections import deque

class WaterDispenser:
    quantity = 0
    water_line = deque()

    def add_person_to_q(self, name: str):
        self.water_line.append(name)
    def refill(self, litters: int):
        self.quantity += litters

    def get_water(self, litters: int):
        if litters <= self.quantity:
            self.quantity -= litters
            return f"{self.water_line.popleft()} got water"
        return f"{self.water_line.popleft()} must wait"

dispenser = WaterDispenser()

dispenser.quantity = int(input())
person = input()

while person != "Start":
    dispenser.add_person_to_q(person)
    person = input()

command = input()
while command != "End":
    if command.isdigit():
        print(dispenser.get_water(int(command)))
    else:
        _, litters_to_refill = command.split()
        dispenser.refill(int(litters_to_refill))
    command = input()
print(f"{dispenser.quantity} liters left")
