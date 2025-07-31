n = int(input())
li = list([0]*n for _ in range(n))
for i in range(n):
    li[i][0] = int(input())
for y in range(1, n):
    for x in range(1, n):
        li[y][x] = li[y][x-1] - li[y-1][x-1]

for y in range(n):
    for x in range(n):
        if x>y:
            continue
        else:
            print(li[y][x], end = ' ')
    print()