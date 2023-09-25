row, col = [int(x) for x in input().split(", ")]
matrix = [[int(x) for x in input().split(", ")] for _ in range(row)]
print(sum(list(map(sum,zip(*matrix)))))

print(matrix)
