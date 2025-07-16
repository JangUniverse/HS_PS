n = int(input())
li = list([0]*n for _ in range(n))
count = 1
res = 0
for y in range(n):
    for x in range(n):
        li[y][x] = count
        if y == 0 or x == 0 or y == n-1 or x == n-1:
            res += count
        count += 1
print(res)
