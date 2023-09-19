number_of_string = int(input())

set_ = set()

for _ in range(number_of_string):
    set_.add(input())
print("\n".join(set_))