import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

s = input().strip()
mod = 10007
n = len(s)
dp = [[0] * n for _ in range(n)]

def find(l, r):
    if l > r:
        return 0
    if l == r:
        return 1
    if dp[l][r]:
        return dp[l][r]
    
    dp[l][r] = (find(l, r-1) + find(l+1, r) - find(l+1, r-1)) % mod
    if s[l] == s[r]:
        dp[l][r] = (dp[l][r] + find(l+1, r-1) + 1) % mod 
    return dp[l][r]

print(find(0, n-1))