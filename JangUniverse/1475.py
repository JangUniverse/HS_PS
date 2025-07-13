a, b = map(int, input().split())
li = list([0]*b for i in range(a))
count = 1

for j in range(b-1, -1, -1):
    col = b-1-j
    if col % 2 == 0:
        for i in range(a):
            li[i][j] = count
            count += 1
            
    else:
        for i in range(a-1, -1, -1):
            li[i][j] = count
            count += 1

for _ in range(a):
    print(*li[_])