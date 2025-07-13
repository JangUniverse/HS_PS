a, b= map(int, input().split())
li = list([0]*b for i in range(a))
cnt = 1
for i in range(a+b-1): #대각선을 지정
    for x in range(0, b):
        for y in range(0, a):
            if x+y == i:
                li[y][x] = cnt
                cnt += 1
for i in range(a):
    print(*li[i])