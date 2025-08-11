import sys
input = sys.stdin.readline

li = [[[0 for _ in range(1024)] for _ in range(101)] for _ in range(10)]

for i in range(1, 10):
    li[i][1][1<<i] = 1

# 1-8 --> i-1, i+1 // 0 --> 1 // 9 --> 8
for i in range(2, 101):
    for j in range(10):
        for k in range(1024):
            if j == 0:
                li[0][i][k|1<<0] += li[1][i-1][k]
                li[0][i][k|1<<0] %= 1000000000
            elif j == 9:
                li[9][i][k|1<<9] += li[8][i-1][k]
                li[9][i][k|1<<9] %= 1000000000
            else:
                li[j][i][k|1<<j] += li[j-1][i-1][k]
                li[j][i][k|1<<j] %= 1000000000
                li[j][i][k|1<<j] += li[j+1][i-1][k]
                li[j][i][k|1<<j] %= 1000000000

n = int(input())
ans = 0

for i in range(10):
    ans += li[i][n][1023]
    ans %= 1000000000

print(ans)