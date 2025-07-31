import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())
net = [[] for _ in range(n+1)]
visit = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    net[a].append(b)
    net[b].append(a)

def bfs():
    q = deque()
    count = 0
    q.append(1)      
    visit[1] = 1
    while q:
        current = q.popleft()
        for val in net[current]:
            if visit[val] == 0:
                q.append(val)
                visit[val] = 1
                count += 1
    print(count)

bfs()
