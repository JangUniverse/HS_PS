#메모리 에반데
import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * (1 << n) for _ in range(n)]
inf = float('inf')

def dfs(now, visited):
    if visited == (1 << n) - 1: 
        return graph[now][0] if graph[now][0] else inf
    
    if dp[now][visited] != -1:  
        return dp[now][visited]
    
    for nxt in range(1, n):
        if graph[now][nxt] and not visited & (1 << nxt):
            cost = graph[now][nxt] + dfs(nxt, visited | (1 << nxt))
            if dp[now][visited] == -1:
                dp[now][visited] = cost
            else:
                dp[now][visited] = min(dp[now][visited], cost)
    
    return dp[now][visited] if dp[now][visited] != -1 else inf

print(dfs(0, 1))