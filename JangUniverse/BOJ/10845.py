import sys
input = sys.stdin.readline
from collections import deque

q = deque()
n = int(input())

for _ in range(n):
    c = list(input().split())
    
    if c[0] == 'push':
        q.append(int(c[1]))
    elif c[0] == 'pop':
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    elif c[0] == 'size':
        print(len(q))
    elif c[0] == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif c[0] == 'front':
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])  
    elif c[0] == 'back':
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1]) 