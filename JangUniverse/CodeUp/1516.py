#python으로 시간 초과 남. pypy로 풀 것.
a, b = map(int, input().split())
p, q, r = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(a)]
k = int(input()) 

dy = [-1, -1, -1, 0, 0, 1, 1, 1]
dx = [-1,  0,  1, -1, 1, -1, 0, 1]

for _ in range(k):
    res = [[0] * b for _ in range(a)]
    for y in range(a):
        for x in range(b):
            life = 0
            for d in range(8):
                ny, nx = y + dy[d], x + dx[d]
                if 0 <= ny < a and 0 <= nx < b:
                    life += matrix[ny][nx]

            if matrix[y][x] == 1:
                res[y][x] = 1 if q <= life < r  else 0  #
            else:
                res[y][x] = 1 if life == p else 0
    matrix = res  # 다음 세대에 업데이트

for row in matrix:
    print(*row)
