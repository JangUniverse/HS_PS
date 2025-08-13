import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    res = 0
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    
    for i in range(n):
        ax, ay, r = map(int, input().split())
        
        d1_sq = (x1 - ax) ** 2 + (y1 - ay) ** 2
        d2_sq = (x2 - ax) ** 2 + (y2 - ay) ** 2
        r_sq = r ** 2
        
        if d1_sq < r_sq and d2_sq < r_sq:
            continue
        elif d1_sq < r_sq or d2_sq < r_sq:
            res += 1

    print(res)