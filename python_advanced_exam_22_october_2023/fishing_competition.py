def is_valid_position(row, col, matrix_size):
    return 0 <= row < matrix_size and 0 <= col < matrix_size

def move_ship(row, col, direction, matrix_size):
    if direction == "up":
        row -= 1
    elif direction == "down":
        row += 1
    elif direction == "left":
        col -= 1
    elif direction == "right":
        col += 1

    if row < 0:
        row = matrix_size - 1
    elif row >= matrix_size:
        row = 0

    if col < 0:
        col = matrix_size - 1
    elif col >= matrix_size:
        col = 0

    return row, col

n = int(input())
fishing_area = []
ship_row, ship_col = 0, 0
fish_caught = 0

for row in range(n):
    line = input()
    fishing_area.append(list(line))
    if 'S' in line:
        ship_row, ship_col = row, line.index('S')

commands = []
while True:
    command = input()
    if command == "collect the nets":
        break
    commands.append(command)

for command in commands:
    fishing_area[ship_row][ship_col] = '-'
    ship_row, ship_col = move_ship(ship_row, ship_col, command, n)

    element = fishing_area[ship_row][ship_col]

    if element.isdigit():
        fish_caught += int(element)
        fishing_area[ship_row][ship_col] = '-'

    if element == 'W':
        print(
            f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [{ship_row},{ship_col}]")
        exit()

    fishing_area[ship_row][ship_col] = 'S'

if fish_caught >= 0:
    print("Success! You managed to reach the quota!")
else:
    print(f"You didn't catch enough fish and didn't reach the quota! You need {20 - fish_caught} tons of fish more.")

print(f"Amount of fish caught: {fish_caught} tons.")
for row in fishing_area:
    print(''.join(row))
