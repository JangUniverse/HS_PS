n = int(input())
li = list([0]*n for i in range(n))
count = 0
row_size, col_size = n,n
row, col = 0, -1
step = 1

while row_size and col_size:
    for i in range(col_size):
        col += step
        count += 1
        li[row][col] = count
    row_size -= 1
    for j in range(row_size):
        row += step
        count += 1
        li[row][col] = count
    col_size -= 1
    step *= -1

for _ in range(n):
    print(*li[_])