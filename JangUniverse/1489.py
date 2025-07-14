a, b= map(int ,input().split())
li = list([0] * b for i in range(a))
count = a*b+1
row_size, col_size = a, b
row, col =  a-1, b
step = -1
while row_size and col_size:
    for i in range(col_size):
        count -= 1
        col += step
        li[row][col] = count
    row_size -= 1
    for j in range(row_size):
        count -= 1
        row += step
        li[row][col] = count
    col_size -= 1
    step *= -1

for i in range(a):
    print(*li[i])