import sys
from collections import deque
input = sys.stdin.readline

def bfs(s):
    q = deque()
    q.append(s)
    visited[s] = 1
    while q:
        x = q.popleft()
        for i in graph[x]:
            if not visited[i]: 
                visited[i] = 1
                q.append(i)

n, m = map(int, input().split())
graph = [[] for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (n+1)
cnt = 0

for i in range(1, n+1):
    if not visited[i]:
        bfs(i)
        cnt += 1

print(cnt)