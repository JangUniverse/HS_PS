n = int(input())
li = list([0]*n for _ in range(n))
count = 1
for x in range(n):
    for y in range(n):
        li[y][x] = count
        count += 1
for y in range(n):
    print(*li[y])