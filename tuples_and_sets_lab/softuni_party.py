number_guest = int(input())

reservation = {input() for _ in range(number_guest)}
guest_who_came = input()

while guest_who_came != "END":
    reservation.remove(guest_who_came)
    guest_who_came = input()

print(len(reservation))
print("\n".join(sorted(reservation)))