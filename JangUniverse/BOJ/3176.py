#트리의 공통조상
import sys
input = sys.stdin.readline
from collections import deque
import math
inf = float('inf')

n = int(input())
k = int(math.log2(n))+1
tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    u, v, w = map(int, input().split())
    tree[u].append((v, w))
    tree[v].append((u, w))

queue = deque([(1,1)])
depth = [0] *(n+1)
depth[1] = 1
dp = [[[0,0,0] for _ in range(k)] for _ in range(n+1)]

while queue:
    i , d = queue.popleft()
    for j, w in tree[i]:
        if not depth[j]:
            queue.append((j, d+1))
            depth[j] = d+1
            dp[j][0] = [i, w, w]
    
for j in range(1, k):
    for i in range(1, n+1):
        dp[i][j][0] = dp[dp[i][j-1][0]][j-1][0]
        dp[i][j][1] = min(dp[i][j-1][1], dp[dp[i][j-1][0]][j-1][1])
        dp[i][j][2] = max(dp[i][j-1][2], dp[dp[i][j-1][0]][j-1][2])

for x in range(int(input())):
    a, b = map(int, input().split())
    maximum = 0
    minimum = inf

    if depth[a] > depth[b]:
        a, b = b, a
    
    for y in range(k-1, -1, -1):
        if depth[b]-depth[a] >= (1<<y):
            minimum = min(minimum, dp[b][y][1])
            maximum = max(maximum, dp[b][y][2])
            b = dp[b][y][0]
    
    if a == b:
        print(minimum, maximum)
        continue
        
    for y in range(k-1, -1, -1):
        if dp[a][y][0] != dp[b][y][0]:
            minimum = min(minimum, dp[a][y][1], dp[b][y][1])
            maximum = max(maximum, dp[a][y][2], dp[b][y][2])
            a = dp[a][y][0]
            b = dp[b][y][0]
    
    minimum = min(minimum, dp[a][0][1], dp[b][0][1])
    maximum = max(maximum, dp[a][0][2], dp[b][0][2])
    print(minimum, maximum)