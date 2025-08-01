import sys
input = sys.stdin.readline

n = int(input())#주변의 색이 달라야 함
li = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * 3 for _ in range(n)]
dp[0] = li[0]
for i in range(1,n):
    dp[i][0] = min(dp[i-1][1],dp[i-1][2]) + li[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) +li[i][1]
    dp[i][2] =min(dp[i-1][0], dp[i-1][1]) + li[i][2]
print(min(dp[-1]))