import sys
import heapq
input = sys.stdin.readline
inf = float('inf')
n, m = map(int, input().split())
li = [[] for _ in range(n+1)]

for _ in range(m):
    s, e, t = map(int, input().split())
    li[s].append((e, t))
    li[e].append((s, t))

a, b = map(int, input().split())

# 다익스트라
dist = [[inf] * 2 for _ in range(n+1)]
heap = []
heapq.heappush(heap, (0, a, 0))  
heapq.heappush(heap, (0, a, 1))
dist[a][0] = 0
dist[a][1] = 0

while heap:
    cost, now, power = heapq.heappop(heap)
    
    if dist[now][power] < cost:
        continue
    
    for next_node, next_power in li[now]:
        if power == next_power:
            next_cost = cost     
        else:
            next_cost = cost + 1
        
        if next_cost < dist[next_node][next_power]:
            dist[next_node][next_power] = next_cost
            heapq.heappush(heap, (next_cost, next_node, next_power))

print(min(dist[b][0], dist[b][1]))