import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(n):
    global cnt
    path.append(n)
    visited[n] = 1
    x = graph[n]
    
    if visited[x] == 0:
        dfs(x)
    elif x in path:
        cycle_start = path.index(x)
        cnt -= len(path[cycle_start:])
    
    path.pop()

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    graph = defaultdict(int)
    visited = defaultdict(int)
    cnt = n
    
    # 그래프 구성 (1-indexed)
    for i in range(n):
        graph[i + 1] = arr[i]
    
    for i in range(1, n + 1):
        if visited[i] == 0:
            path = [] 
            dfs(i)
    
    print(cnt)