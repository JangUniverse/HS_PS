import sys
input = sys.stdin.readline
inf = float('inf')
N = int(input())
M = int(input())
graph =  [list([inf] * (N+1)) for _ in range(N+1) ]

for i in range(M):
    a, b, c = map(int, input().split())
    if graph[a][b] > c:
        graph[a][b] = c

for i in range(1, N+1):
    graph[i][i] = 0

def floyd():
    for cp in range(1, N+1): #cp means 경유지
        for s in range(1, N+1):
            for e in range(1, N+1):
                if graph[s][e] > graph[s][cp] + graph[cp][e]:
                    graph[s][e] =  graph[s][cp] + graph[cp][e]

floyd()
for i in range(1, N+1):
    for j in range(1, N+1):
        if graph[i][j] == inf:
            graph[i][j] = 0

for i in range(1, N+1):
    print(*graph[i][1:])