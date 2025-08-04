import sys
from collections import deque, defaultdict
input = sys.stdin.readline

n,m = map(int, input().split())
#존재하지 않는 키에 접근할 때 자동으로 기본값을 생성해주는 딕셔너리입니다.
o = defaultdict(int)
graph = defaultdict(list)

for i in range(m):
    a, b = map(int ,input().split())
    graph[a].append(b)
    o[b] += 1

que = deque() 
for i in range(1, n+1):
    if not o[i]:
        que.append(i)
while que:
    v = que.popleft()
    print(v, end=' ')
    for x in graph[v]:
        o[x] -= 1

        if o[x] == 0:
            que.append(x)