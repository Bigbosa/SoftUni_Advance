string = input()

stack = []

for index, char in enumerate(string):
    if char == "(":
        stack.append(index)
    elif char == ")":
        start_index = stack.pop()
        print(string[start_index:1 + index])