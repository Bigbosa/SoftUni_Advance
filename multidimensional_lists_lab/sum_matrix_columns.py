row, col = [int(x) for x in input().split(", ")]
result = list(map(sum, zip(*[[int(x) for x in input().split()]for _ in range(row)])))
[print(x) for x in result]