import sys
inf = float('inf')
input = sys.stdin.readline

c, n = map(int, input().split())
li = []
for _ in range(n):
    cost, customer = map(int, input().split())
    li.append((cost, customer))

dp = [inf] * (c + 101)
dp[0] = 0

for cost, customer in li:
    for j in range(customer, c + 101): 
        if dp[j - customer] != inf:
            dp[j] = min(dp[j], dp[j - customer] + cost)

print(min(dp[c:]))