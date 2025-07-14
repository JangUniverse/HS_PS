a, b = map(int, input().split())
li = [[0] * b for _ in range(a)]

count = a * b
row_size, col_size = a, b
step = 1
row, col = 0, -1

while row_size and col_size:
    for _ in range(col_size):
        col += step
        li[row][col] = count
        count -= 1
    row_size -= 1

    for _ in range(row_size):
        row += step
        li[row][col] = count
        count -= 1
    col_size -= 1

    step *= -1

for row in li:
    print(*row)
