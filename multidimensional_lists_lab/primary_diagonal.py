row = int(input())
matrix = [[x for x in input().split()] for _ in range(row)]
[print(sum(int(matrix[i][i]) for i in range(row)))]