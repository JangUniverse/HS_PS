import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    q = deque()
    q.append(1)
    visited[1] = 1
    
    while q:
        x = q.popleft()
        for i in li[x]:
            if visited[i] == 0:
                visited[i] = 1
                graph[i] = x  
                q.append(i)
    return graph[2:]

n = int(input())
visited = [0] * (n+1)
graph = [0] * (n+1)

li = [[] for i in range(n+1)] 
for i in range(n-1):
    a, b = map(int, input().split())
    li[a].append(b)
    li[b].append(a)

result = bfs()  
print('\n'.join(map(str, result))) 