import sys
input =sys.stdin.readline


n = int(input())
li = list()
for i in range(n):
    li.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            li[i][j] = li[i-1][j] + li[i][j]
        elif j == i:
            li[i][j] = li[i-1][j-1] + li[i][j]
        else:
            li[i][j] = max(li[i-1][j], li[i-1][j-1]) + li[i][j]

print(max(li[n-1]))