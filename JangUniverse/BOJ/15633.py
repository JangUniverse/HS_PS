import sys
input = sys.stdin.readline
def dfs(k):
    if k == m:
        print(*li)
        return
    tmp = 0
    for i in range(n):
        if not visited[i] and tmp != li[i]:
            ans[k] = li[i]
            visited[i] = 1
            tmp = li[i]
            dfs(k+1)
            visited[i] = False
            
n, m = map(int, input().split())
li = list(map(int, input().split()))
visited = []*n
ans = [-1]*10