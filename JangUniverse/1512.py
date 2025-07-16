n = int(input())
a, b= map(int, input().split())#a-->y
a -= 1
b -= 1
li = list([0]*n for i in range(n))
for y in range(n):
    for x in range(n):
        li[y][x] = abs(a-y)+abs(b-x)+1
for i in range(n):
    print(*li[i])