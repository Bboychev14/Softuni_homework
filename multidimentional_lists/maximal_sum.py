rows, cols = [int(x) for x in input().split()]
matrix = []

for _ in range(rows):
    numbers = [int(x) for x in input().split()]
    matrix.append(numbers)
max_sum = 0
best_row = 0
best_col = 0
for row in range(rows - 2):
    for col in range(cols - 2):
        temp_sum = 0
        temp_sum += matrix[row][col] + matrix[row][col + 1] + matrix[row][col + 2] + \
                    matrix[row + 1][col] + matrix[row + 1][col + 1] + matrix[row + 1][col + 2] + \
                    matrix[row + 2][col] + matrix[row + 2][col + 1] + matrix[row + 2][col + 2]
        if temp_sum > max_sum:
            max_sum = temp_sum
            best_row = row
            best_col = col
print(f"Sum = {max_sum}")
print(f"{matrix[best_row][best_col]} {matrix[best_row][best_col + 1]} {matrix[best_row][best_col + 2]} ")
print(f"{matrix[best_row + 1][best_col]} {matrix[best_row + 1][best_col + 1]} {matrix[best_row + 1][best_col + 2]} ")
print(f"{matrix[best_row + 2][best_col]} {matrix[best_row + 2][best_col + 1]} {matrix[best_row + 2][best_col + 2]} ")