import sys
input = sys.stdin.readline
max_d = 100000
log = 0
while 2**log <= max_d:
    log += 1

n = int(input())
graph = [[] for _ in range(n+1)]

for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

tree = [[0 for _ in range(log)] for _ in range(n+1)]
visit = [1]
level = [-1] * (n+1)
level[1] = 0 
while visit:
    now = visit.pop()
    
    for nxt in graph[now]:
        if level[nxt] != -1:
            continue
        
        level[nxt] = level[now] + 1  
        tree[nxt][0] = now           
        visit.append(nxt)

for i in range(1, log):
    for j in range(1, n+1):
        tree[j][i] = tree[tree[j][i-1]][i-1]

m = int(input())
for i in range(m):
    a, b = map(int, input().split())
    
    if level[a] < level[b]:
        a, b = b, a
    
    for j in range(log-1, -1, -1):
        if level[a] - level[b] >= 2**j:
            a = tree[a][j]
    
    if a == b:
        print(a)
        continue
    
    for j in range(log-1, -1, -1):
        if tree[a][j] != tree[b][j]:
            a = tree[a][j]
            b = tree[b][j]
    
    print(tree[a][0])