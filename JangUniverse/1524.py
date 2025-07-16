check = [list(map(int, input().split())) for i in range(9)]
x, y = map(int, input().split())
x -= 1
y -= 1
if check[x][y] == 1:
    print(-1)
else:
    tmp = []
    dy = [-1, -1, -1, 0, 0, 1, 1, 1]
    dx = [-1,  0,  1, -1, 1, -1, 0, 1]

    for d in range(8):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < 9 and 0 <= ny < 9:
            tmp.append(check[nx][ny])

    print(tmp.count(1))
