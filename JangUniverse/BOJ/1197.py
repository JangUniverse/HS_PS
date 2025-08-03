import sys
import heapq
input= sys.stdin.readline
sys.setrecursionlimit(10**6)

v, e= map(int, input().split())
heap = []
for i in range(e):
    a, b, t = map(int, input().split())
    heapq.heappush(heap, [t, a, b])
root = [i for i in range(v+1)]

#union + kruskal
def find(n):
    if n == root[n]:
        return n
    root[n] = find(root[n])
    return root[n]

def union(n1, n2):
    n1= find(n1)
    n2 = find(n2)

    if n1<n2:
        root[n2] = n1
    else:
        root[n1] = n2
ans = 0
while heap:
    wei, n1, n2 = heapq.heappop(heap)
    if find(n1) != find(n2):
        union(n1, n2)
        ans += wei
print(ans)