matrix = [list(map(int, input().split())) for _ in range(25)]
res = [[0] * 25 for _ in range(25)]

dy = [-1, -1, -1,  0, 0, 1, 1, 1]
dx = [-1,  0,  1, -1, 1, -1, 0, 1]

for y in range(25):
    for x in range(25):
        life = 0
        for d in range(8):
            ny, nx = y + dy[d], x + dx[d]
            if 0 <= ny < 25 and 0 <= nx < 25:
                life += matrix[ny][nx]
        if matrix[y][x] == 1:
            res[y][x] = 1 if life == 2 or life == 3 else 0
        else:
            res[y][x] = 1 if life == 3 else 0

for row in res:
    print(*row)
