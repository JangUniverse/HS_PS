import sys
input  = sys.stdin.readline
#when n>3: f(n) = f(n-1) + f(n-2) + f(n-3)
dp = [1, 2, 4]
for i in range(3, 11):
    dp.append(dp[i-1]+dp[i-2]+dp[i-3])

n = int(input())
for i in range(n):
    print(dp[int(input())-1])
    