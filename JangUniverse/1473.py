a, b = map(int, input().split())
li = [[0] * b for _ in range(a)]
count = 1

for i in range(a):
    row = a - 1 - i  #row를 강제로 잡아야 하는 유형 
    if i % 2 == 0: 
        for j in range(b):
            li[row][j] = count
            count += 1
    else: 
        for j in range(b - 1, -1, -1):
            li[row][j] = count
            count += 1

for row in li:
    print(*row)
