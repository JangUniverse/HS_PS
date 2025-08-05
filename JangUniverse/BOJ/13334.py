import sys
import heapq

input = sys.stdin.readline
ans = 0
n = int(input())
road = []
li = []
for _ in range(n):
    li.append(sorted(list(map(int, input().split()))))#sorted 필수
length = int(input())

for r in li:
    s, e = r
    if (e-s) <= length:
        road.append(r)
road.sort(key=lambda x:x[1])
heap = []

for r in road:
    if not heap:
        heapq.heappush(heap, r)
    else:
        while heap[0][0] < r[1]- length:
            heapq.heappop(heap)
            if not heap:
                break
        
        heapq.heappush(heap, r)
    ans = max(ans, len(heap))
print(ans)
