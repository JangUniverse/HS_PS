a, b, m, n = map(int ,input().split()) 
li = [list(map(int, input().split())) for _ in range(b)]

res = 0

for y in range(b - n + 1):  # 세로: y부터 y+n-1까지
    for x in range(a - m + 1):  # 가로: x부터 x+m-1까지
        ka = 0
        for j in range(y, y + n):
            for i in range(x, x + m):#이게 핵심
                ka += li[j][i]
        res = max(res, ka)

print(res)