import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    q = deque()
    q.append(n)
    dist[n] = 0  # 시작점 거리 설정
    
    while q:
        x = q.popleft()
        if x == k:
            print(dist[x])
            return
            
        for j in (x-1, x+1, x*2):
            if 0 <= j <= MAX and dist[j] == -1:
                dist[j] = dist[x] + 1
                q.append(j)

MAX = 100000
n, k = map(int, input().split())
dist = [-1] * (MAX + 1) 

if n == k: 
    print(0)
else:
    bfs()