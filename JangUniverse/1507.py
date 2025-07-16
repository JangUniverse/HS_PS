li = [list(map(int, input().split())) for i in range(4)]
res = [[0]*100 for _ in range(100)]
count = 0

for i in li:
    x1, y1, x2, y2 = i[0], i[1], i[2], i[3]
    for y in range(y1, y2):  # y2 제외
        for x in range(x1, x2):  # x2 제외
            res[y][x] = 1

for y in range(100):
    for x in range(100):
        if res[y][x] == 1:
            count += 1

print(count)
