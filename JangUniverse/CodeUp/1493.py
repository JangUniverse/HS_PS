a, b = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(a)]
arr2  = list([0]*b for i in range(a))

for y in range(a):
    for x in range(b):
        for k in range(y+1):
            for z in range(x+1):
                arr2[y][x] += arr[k][z]

for i in range(a):
    print(*arr2[i])