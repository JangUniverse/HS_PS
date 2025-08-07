import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
inf = float('inf')

v, e= map(int, input().split())
visit = [inf] *(v+1)
order = 0
ans = set()
edge = defaultdict(list)

for i in range(e):
    a, b= map(int ,input().split())
    edge[a].append(b)
    edge[b].append(a)

def dfs(n, isroot):
    global order
    visit[n] = order
    order += 1
    n_child = 0
    child = visit[n]

    for nxt in edge[n]:
        if visit[nxt] < inf:
            child = min(child,  visit[nxt])
        else:
            n_child += 1
            tmp =dfs(nxt, False)
            if not isroot and tmp >= visit[n]:
                ans.add(n)
            child = min(child, tmp)
        
    if isroot and n_child >=  2:
        ans.add(n)
    return child

for i in range(v):
    if visit[i] == inf:
        dfs(i, True)
ans = sorted(list(ans))
print(len(ans))
print(*ans)