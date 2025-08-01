import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if matrix[nx][ny] == 0:
                matrix[nx][ny] = matrix[x][y] + 1
                q.append((nx, ny))

m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
q = deque()
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            q.append((i, j))

bfs()

result = 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0:
            print(-1)
            exit()
        result = max(result, matrix[i][j])

print(result - 1)