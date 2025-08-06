import sys
import heapq
from collections import deque
input = sys.stdin.readline
inf = float('inf')
#다익 --> bfs로 거른  다음에 다익 다시 돌리면 될듯


def dijkstra():
    q = []
    heapq.heappush(q, (0, st))
    dist = [inf] * n
    dist[st] = 0

    while q:
        d, now = heapq.heappop(q)
        if dist[now] < d:
            continue
        for nxt, w in graph[now]:
            if visited[now][nxt]:
                continue
            cost = d + w


            if cost < dist[nxt]:
                dist[nxt] = cost
                heapq.heappush(q, (cost, nxt))#괄호야발
    return dist

def bfs():

    q = deque()
    q.append(ed)


    while q:
        v = q.popleft()
        if v == st:
            continue

        
        for node, cost in rev_graph[v]:
            if dist[node] + cost == dist[v] and not visited[node][v]:
                visited[node][v] = True
                q.append(node)

while True:
    n, m = map(int, input().split())
    if not n and not m:
        break
    
    st, ed = map(int, input().split())
    graph = [[] for _ in range(n)]
    rev_graph = [[] for _ in range(n)]
    
    visited = [[False] * n for _ in range(n)]
    
    for i in range(m):
        s, e, v = map(int, input().split())
        graph[s].append((e, v))
        rev_graph[e].append((s, v))
    
    dist = dijkstra()
    bfs()
    dist = dijkstra()
    
    if dist[ed] == inf:
        print(-1)
    else:
        print(dist[ed])