import sys
input = sys.stdin.readline
inf = float('inf')
n = int(input())
li = list(map(int, input().split()) for _ in range(n))
for x1, y1, r1, x2, y2, r2 in li:
    res = (abs(x1-x2)**2+abs(y1-y2)**2)**0.5
    
    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
        continue

    elif res + r1 < r2 or res + r2 < r1:
        print(0)
        continue
    elif res + r1 == r2 or res + r2 == r1:
        print(1)
        continue
    elif res > r1+r2:
        print(0)
        continue
    elif res == r1+r2:
        print(1)
        continue
    else:
        print(2)
        continue