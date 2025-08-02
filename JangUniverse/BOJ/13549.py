import sys
import heapq
input =sys.stdin.readline
inf = float('inf')

N, K = map(int, input().split())
dist = [inf]* 100001
heap = []
    
def dijkstra(N, K):
    if K <= N:
        print(N-K)
        return
    dist[N] = 0
    heapq.heappush(heap, (0, N))#time, location
    while heap:
        w, n = heapq.heappop(heap)
        if dist[n] < w:  # 이미 더 짧은 경로로 방문한 경우 스킵
            continue
        for nx in [(n+1, 1), (n-1, 1), (n*2, 0)]: #location, time
            if 0 <= nx[0] <= 100000 and dist[nx[0]] > w + nx[1]:
                dist[nx[0]] = w + nx[1]
                heapq.heappush(heap, (dist[nx[0]], nx[0]))
    print(dist[K])
    return

dijkstra(N, K)