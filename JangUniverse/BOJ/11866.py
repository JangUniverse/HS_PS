import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
q = deque()
res = list()

for i in range(1, n+1):
    q.append(i)
while q:
    for _ in range(k-1):
        q.append(q.popleft())
    res.append(q.popleft())

# 출력 형식: <1, 2, 3, 4, 5, 6, 7>
print('<' + ', '.join(map(str, res)) + '>')