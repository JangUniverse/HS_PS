n = int(input())
li = list([0]*n for _ in range(n))
count = 1
for i in range(n):
    for j in range(n):
        li[i][j] = count
        count += 1

for i in range(n):
    print(*li[i])