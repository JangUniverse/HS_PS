import sys
input = sys.stdin.readline
import heapq
from collections import deque

n, k = map(int, input().split())
bosuk = deque()
for _ in range(n):
    m, v = map(int, input().split())
    bosuk.append((m, v))

gabang = []
for _ in range(k):
    gabang.append(int(input()))

bosuk = deque(sorted(bosuk))
gabang.sort()

heap = []
ans = 0

for b in gabang:
    while bosuk and bosuk[0][0] <= b:
        m, v = bosuk.popleft()
        heapq.heappush(heap, -v)
    
    if heap:
        ans -= heapq.heappop(heap)

print(ans)