from collections import deque

quantity = int(input())
orders = deque(int(x) for x in input().split())

print(max(orders))

while orders:
    orders_number = orders.popleft()
    if quantity - orders_number >= 0:
        quantity-= orders_number
    else:
        print(f"Orders left: {orders_number}", *orders)
        break
else:
    print("Orders complete")