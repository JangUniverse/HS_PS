import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):  
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

art = []
dfsn = [0] * (n+1)
idx = 1

def dfs(c, p):
    global idx
    dfsn[c] = idx
    low = idx
    idx += 1

    for nxt in graph[c]:
        if nxt == p:
            continue
        
        if dfsn[nxt]:  # 이미 방문한 노드
            low = min(low, dfsn[nxt])
        else: 
            child_low = dfs(nxt, c)
            low = min(low, child_low)
            
            # 단절선 조건: dfsn[c] < child_low
            if dfsn[c] < child_low:
                edge = tuple(sorted([c, nxt]))
                art.append(edge)
    
    return low
for i in range(1, n+1):
    if not dfsn[i]:
        dfs(i, 0)

art.sort()
print(len(art))
for ㅑ in art:
    print(*ㅑ)