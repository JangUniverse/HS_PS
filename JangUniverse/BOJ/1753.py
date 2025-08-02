import sys
import heapq
input = sys.stdin.readline
inf = float('inf')

def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))  # (거리, 노드)
    dist[start] = 0
    
    while heap:
        w, n = heapq.heappop(heap)  # (현재까지거리, 현재노드)

        if dist[n] < w:
            continue
    
        for i in graph[n]:
            cost = w + i[1]  # 현재거리 + 간선가중치
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                heapq.heappush(heap, (cost, i[0]))

v, e = map(int, input().split())
start = int(input())
graph = [[] for i in range(v+1)]
dist = [inf] * (v+1)

for i in range(e):
    u, to, w = map(int, input().split())
    graph[u].append((to, w))

dijkstra(start)

# 결과 출력
for i in range(1, v+1):
    if dist[i] == inf:
        print("INF")
    else:
        print(dist[i])