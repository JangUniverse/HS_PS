board = [list(map(int, input().split())) for _ in range(10)]
res = [[0] * 10 for _ in range(10)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for i in range(10):
    for j in range(10):
        if board[i][j] == -1:
            res[i][j] = -1

for i in range(10):
    for j in range(10):
        if board[i][j] > 0:
            res[i][j] = -2 
            power = board[i][j]
            for d in range(4):
                for p in range(1, power + 1):
                    ny, nx = i + dy[d] * p, j + dx[d] * p
                    if 0 <= ny < 10 and 0 <= nx < 10:
                        if res[ny][nx] == -1: break
                        res[ny][nx] = -2
                    else:
                        break
n = int(input())
status = []

for pid in range(1, n + 1):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    if res[x][y] == -2:
        status.append("dead")
    else:
        status.append("survive")
        res[x][y] = pid
for row in res:
    print(*row)
print("Character Information")
for i in range(n):
    print(f"player {i+1} {status[i]}")
