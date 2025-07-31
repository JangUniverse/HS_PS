n = int(input())
li = list([0]*n for i in range(n))
row_size, col_size =n ,n 
row, col = -1, 0
step = 1
count = 0
while row_size and col_size:
    for i in range(row_size):
        count += 1
        row += step
        li[row][col] = count
    col_size -= 1
    for j in range(col_size):
        count += 1
        col += step
        li[row][col] = count
    row_size -= 1
    step *= -1
for i in range(n):
    print(*li[i])
        