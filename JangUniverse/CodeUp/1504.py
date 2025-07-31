n = int(input())
li = list([0] *n for i in range(n))
count = 1
for x in range(n):
    if x %2 == 0:
        for y in range(n):
            li[y][x] = count
            count += 1
    else:
        for y in range(n-1, -1, -1):
            li[y][x] = count
            count +=1
for y in range(n):
    print(*li[y])