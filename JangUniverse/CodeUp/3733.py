import sys
input = sys.stdin.readline
dp = [0]*10000001
dp[1] = 1

def f(n):
    if n < len(dp) and dp[n]:
        return dp[n]
    if n % 2 == 0:
        m = n // 2
    else:
        m = n * 3 + 1
    length = f(m) + 1
    if n < len(dp):
        dp[n] = length
    return length

a, b = map(int, input().split())
max_len = 0
res = a
for i in range(a, b + 1):
    length = f(i)
    if length > max_len:
        max_len = length
        res = i
print(res, max_len)