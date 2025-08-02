import sys
input =sys.stdin.readline

t = int(input())
for i in range(t):
    li = list()
    n = int(input())
    for j in range(2):
        li.append(list(map(int, input().split())))
    for i in range(1, n):
        # if i == 0 --> 이미 되있잖아
        if i == 1:
            li[0][1] += li[1][0]
            li[1][1] += li[0][0]
        else:
            li[0][i] += max(li[1][i-1], li[1][i-2])
            li[1][i] += max(li[0][i-1], li[0][i-2])
    print(max(li[0][n-1], li[1][n-1]))
            