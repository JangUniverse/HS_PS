import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(input().strip()))

visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    q = deque()
    q.append((0, 0, 0))
    visited[0][0][0] = 1

    while q:
        x, y, wall_broken = q.popleft()

        if x == n-1 and y == m-1:
            return visited[x][y][wall_broken]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if graph[nx][ny] == '1':
                if wall_broken == 0 and visited[nx][ny][1] == 0:
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    q.append((nx, ny, 1))
            
            else: 
                if visited[nx][ny][wall_broken] == 0:
                    visited[nx][ny][wall_broken] = visited[x][y][wall_broken] + 1
                    q.append((nx, ny, wall_broken))
    
    return -1

print(bfs())