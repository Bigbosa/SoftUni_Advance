rows , cols = [int(x) for x in input().split()]
square_matrix = [input().split() for _ in range(rows)]
all_square_matrices = 0

def check_valid_index(row, col):
    if 0 <= row + 2 <= rows and 0 <= col +2 <= cols:
        return True

def find_identical_chars(row, col, all_square_matrices):
    if check_valid_index(row, col):
        if all([True if x == square_matrix[row][col:col+2][0] else False for x in
                square_matrix[row][col:col + 2] + square_matrix[row + 1][col:col + 2]]):
            all_square_matrices += 1
    return all_square_matrices

for row in range(rows):
    for col in range(cols):
        all_square_matrices = find_identical_chars(row, col, all_square_matrices)

print(all_square_matrices)