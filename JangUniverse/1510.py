n  = int(input())
li = list([0]*n for i in range(n))
count = 1
row = 0
col = n//2
for i in range(n*n):
    li[row][col] = count
    if count %n == 0:
        row = 0 if row+1>n-1 else row+1
    else:
        row = n-1 if row-1<0 else row-1
        col = 0 if col+1>n-1 else col+1
    count += 1
for _ in range(n):
    print(*li[_])