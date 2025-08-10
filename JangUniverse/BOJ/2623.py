import sys
from collections import defaultdict, deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = defaultdict(list)
weight = defaultdict(int)

for i in range(m):
    cnt = list(map(int, input().split()))
    for j in range(1, cnt[0]):
        a = cnt[j]
        b = cnt[j+1]
        graph[a].append(b)
        weight[b] += 1

que = deque()
res = []

for i in range(1, n+1):
    if weight[i] == 0:
        que.append(i)

while que:
    v = que.popleft()
    res.append(v)

    for next_node in graph[v]:
        weight[next_node] -= 1
        
        if weight[next_node] == 0:
            que.append(next_node)

if len(res) == n:
    for singer in res:
        print(singer)
else:
    print(0)