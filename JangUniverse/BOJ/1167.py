import sys
input = sys.stdin.readline
from collections import deque

v = int(input())
tree = [[] for _ in range(v+1)]

for i in range(v):
    n = list(map(int, input().split()))
    for j in range(1, len(n)-1, 2):
        tree[n[0]].append((n[j], n[j+1]))

def bfs(x):
    visited = [-1] * (v+1)
    q = deque()
    q.append(x)
    visited[x] = 0
    dist = [0, 0]

    while q:
        n = q.popleft()
        for a, b in tree[n]:
            if visited[a] == -1:
                visited[a] = visited[n] + b
                q.append(a)
                
                if visited[a] > dist[1]:
                    dist = [a, visited[a]]
    
    return dist

node = bfs(1)
print(bfs(node[0])[1])