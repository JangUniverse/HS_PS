import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(n, w):
    for weight, n in tree[n]:
        if dist[n] == -1:
            dist[n] = weight + w
            dfs(n, weight+w)



n = int(input())
tree = [[]  for _ in range(n+1)]
for i in range(n-1):

    x, y, z= map(int, input().split())
    tree[x].append((z, y))
    tree[y].append((z, x))

dist = [-1] * (n+1)
dist[1] = 0
dfs(1, 0)

s = dist.index(max(dist))
dist = [-1] * (n+1)
dist[s] = 0
dfs(s, 0)

print(max(dist))