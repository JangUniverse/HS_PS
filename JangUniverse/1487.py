a, b= map(int, input().split())
li = list([0]*b for _ in range(a))
count = a*b+1
row, col = -1, b-1
row_size, col_size = a ,b
step = 1
while row_size and col_size:
    for i in range(row_size):
        count -= 1
        row += step
        li[row][col] = count
    step *= -1
    col_size -= 1
    for j in range(col_size):
        count -= 1
        col += step
        li[row][col] = count
    row_size -= 1
for i in range(a):
    print(*li[i])