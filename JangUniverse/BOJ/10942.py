import sys
input = sys.stdin.readline

n = int(input())
num = [0] + list(map(int, input().split()))
m = int(input())

dp = [[0] * (n+1) for _ in range(n+1)]

# 길이 1인 경우
for i in range(1, n+1):
    dp[i][i] = 1

# 길이 2인 경우  
for i in range(1, n):
    if num[i] == num[i+1]:
        dp[i][i+1] = 1

# 길이 3 이상인 경우
for length in range(3, n+1):
    for i in range(1, n-length+2):
        j = i + length - 1
        if num[i] == num[j] and dp[i+1][j-1]:
            dp[i][j] = 1

for _ in range(m):
    s, e = map(int, input().split())
    print(dp[s][e])