import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
graph = [[] for _ in range(n+1)]
for i in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dp = [[0, 0] for _ in range(n+1)]  # [얼리어답터X, 얼리어답터O]
visited = [0] * (n+1)

def dfs(node):
    visited[node] = 1
    dp[node][0] = 0 
    dp[node][1] = 1 
    for child in graph[node]:
        if not visited[child]:
            dfs(child)
            # 현재 노드가 얼리어답터가 아니면 자식은 무조건 얼리어답터여야 함
            dp[node][0] += dp[child][1]
            # 현재 노드가 얼리어답터면 자식은 얼리어답터이거나 아니거나 상관없음
            dp[node][1] += min(dp[child][0], dp[child][1])

dfs(1)
print(min(dp[1]))