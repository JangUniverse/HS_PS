a, b = map(int, input().split())
li = list([0]*b for _ in range(a))
count = 1
for i in range(b-1, -1, -1):
    for j in range(a-1, -1, -1):
        li[j][i] = count
        count += 1

for i in range(a):
    print(*li[i])