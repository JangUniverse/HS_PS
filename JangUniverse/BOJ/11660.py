import sys
input = sys.stdin.readline

n, m = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(n)]
dp = list([0] * (n+1) for _ in range(n+1))


for r in range(1, n+1):
    for c in range(1, n+1):
        dp[r][c] = li[r-1][c-1]+ dp[r-1][c] + dp[r][c-1] - dp[r-1][c-1] #li만 0 based index

for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    res = dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1]
    print(res)
