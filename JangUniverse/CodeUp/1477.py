a, b = map(int, input().split())
li = list([0]*b for i in range(a))
count = 1
for i in range(a+b-1):
    for y in range(a):
        for x in range(b):
            if x + y == i:
                li[y][x] = count 
                count += 1
for i in range(a):
    print(*li[i])