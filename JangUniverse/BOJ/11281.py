import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def convert(x, n):
    if x < 0:
        return -x - 1 + n
    else:
        return x - 1

def negate(x, n):
    return (x + n) % (2 * n)

n, m = map(int, input().split())
graph = [[] for _ in range(2 * n)]

for _ in range(m):
    a, b = map(int, input().split())
    a = convert(a, n)
    b = convert(b, n)
    graph[negate(a, n)].append(b)
    graph[negate(b, n)].append(a)

visited = [False] * (2 * n)
finished = [False] * (2 * n)
stack = []
scc_id = [-1] * (2 * n)
id_cnt = 0
scc_cnt = 0
ids = [0] * (2 * n)

def scc(node):
    global id_cnt, scc_cnt
    ids[node] = low = id_cnt
    id_cnt += 1
    visited[node] = True
    stack.append(node)

    for nxt in graph[node]:
        if finished[nxt]:
            continue
        if visited[nxt]:
            low = min(low, ids[nxt])
        else:
            low = min(low, scc(nxt))

    if low == ids[node]:
        while stack:
            top = stack.pop()
            finished[top] = True
            scc_id[top] = scc_cnt
            if top == node:
                break
        scc_cnt += 1
    
    return low

for i in range(2 * n):
    if not visited[i]:
        scc(i)

for i in range(n):
    if scc_id[i] == scc_id[negate(i, n)]:
        print(0)
        exit()

print(1)
res = [0] * n
for i in range(n):
    if scc_id[i] < scc_id[negate(i, n)]:
        res[i] = 1

print(*res)