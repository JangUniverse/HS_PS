def f(n, a, dp):
    if n == 1:
        dp[1] = a[1]
        return dp[1]
    elif n == 2:
        dp[2] = a[1] + a[2]
        return dp[2]
    elif n == 3:
        dp[3] = max(a[1] + a[3], a[2] + a[3])
        return dp[3]

    if dp[n] != -1:
        return dp[n]
    else:
        dp[n] = max(f(n-3, a, dp) + a[n-1] + a[n], f(n-2, a, dp) + a[n])
        return dp[n]

n = int(input())
a = [0]  
for _ in range(n):
    a.append(int(input()))

dp = [-1] * (n + 1)

print(f(n, a, dp))
