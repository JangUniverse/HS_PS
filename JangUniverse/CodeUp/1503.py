n = int(input())
li = list([0] *n for i in range(n))
count = 1
for y in range(n):
    if y %2 == 0:
        for x in range(n):
            li[y][x] = count
            count += 1
    else:
        for x in range(n-1, -1, -1):
            li[y][x] = count
            count +=1
for y in range(n):
    print(*li[y])