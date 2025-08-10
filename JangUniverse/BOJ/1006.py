import sys
input = sys.stdin.readline

def calc(start, a, b, c):
    for i in range(start, n):
        a[i+1] = min(b[i]+1, c[i]+1)
        if zone1[i] + zone2[i] <= w: 
            a[i+1] = min(a[i+1], a[i]+1)
        if i > 0 and zone1[i-1] + zone1[i] <= w and zone2[i-1] + zone2[i] <= w: 
            a[i+1] = min(a[i+1], a[i-1]+2)

        if i < n-1:
            b[i+1] = a[i+1] + 1
            if zone1[i+1] + zone1[i] <= w: 
                b[i+1] = min(b[i+1], c[i] + 1)
            
            c[i+1] = a[i+1]+1
            if zone2[i+1] + zone2[i] <= w: 
                c[i+1] = min(c[i+1], b[i] + 1)
    return a, b, c

t = int(input())
for _ in range(t):
    n, w = map(int, input().split())
    zone1 = list(map(int, input().split()))
    zone2 = list(map(int, input().split()))
    
    a = [0] * (n+1)
    b = [0] * (n+1)
    c = [0] * (n+1)
    a[0] = 0
    b[0] = 1
    c[0] = 1
    
    a, b, c = calc(0, a, b, c)
    res = a[n]
    
    if n > 1 and zone1[0] + zone1[n-1] <= w:
        a = [0] * (n+1) 
        b = [0] * (n+1)
        c = [0] * (n+1)
        a[1] = 1
        b[1] = 2
        c[1] = 1 if zone2[0] + zone2[1] <= w else 2
        a, b, c = calc(1, a, b, c)
        res = min(res, c[n-1] + 1)
        
    if n > 1 and zone2[0] + zone2[n-1] <= w:
        a = [0] * (n+1) 
        b = [0] * (n+1)
        c = [0] * (n+1)
        a[1] = 1
        c[1] = 2
        b[1] = 1 if zone1[0] + zone1[1] <= w else 2
        a, b, c = calc(1, a, b, c)
        res = min(res, b[n-1] + 1)

    if n > 1 and zone1[0] + zone1[n-1] <= w and zone2[0] + zone2[n-1] <= w:
        a = [0] * (n+1) 
        b = [0] * (n+1)
        c = [0] * (n+1)
        a[1] = 0
        b[1] = 1
        c[1] = 1
        a, b, c = calc(1, a, b, c)
        res = min(res, a[n-1] + 2)
    
    print(res)