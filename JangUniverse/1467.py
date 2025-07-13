a, b = map(int, input().split())
li = list([0] * b for _ in range(a))
count = 1
for j in range(b-1, -1, -1):
    for i in range(a):
        li[i][j] = count
        count += 1
    
for _ in range(a):
    print(*li[_])