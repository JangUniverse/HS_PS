import sys
import heapq
input = sys.stdin.readline
inf = float('inf')


N, M, X  = map(int, input().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))

def dijkstra(s):
    dist = [inf]*(N+1)
    dist[s] = 0
    heap = [(0, s)] 
    while heap:
        d, n = heapq.heappop(heap)
        if dist[n] < d:  
            continue
        for v, val in graph[n]:
            cost = d + val
            if cost < dist[v]:  
                dist[v] = cost
                heapq.heappush(heap, (cost, v))
    return dist

res = dijkstra(X)
for i in range(1, N+1):
    if i != X:
        go_dist = dijkstra(i)  
        res[i] += go_dist[X]   # 가는 시간 + 오는 시간

res[X] = 0  # X에서 X로는 0
print(max(res[1:]))
