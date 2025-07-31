a, b = map(int, input().split())
li = [[0]*b for _ in range(a)]

count = 0
step = 1
row_size, col_size = a, b
row, col = -1, b - 1 
while row_size and col_size:
    for _ in range(row_size):
        row += step
        count += 1
        li[row][col] = count
    col_size -= 1

    for _ in range(col_size):
        col -= step
        count += 1
        li[row][col] = count
    row_size -= 1

    step *= -1

for row in li:
    print(*row)
