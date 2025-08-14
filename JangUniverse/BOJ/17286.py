import sys
from itertools import permutations
input = sys.stdin.readline
inf = float('inf')

res = inf
x = list()
y = list()

for _ in range(4):
    a, b = map(int ,input().split())
    x.append(a)
    y.append(b)
for p in permutations([1,2,3],3):
    X = x[0]
    Y = y[0]
    m = 0

    for i in p:
        #맨해튼이 아니었어?
        m += (abs(X-x[i]) ** 2 + abs(Y-y[i]) **2 ) ** 0.5
        X = x[i]
        Y = y[i]
    
    res = min(res, int(m))

print(res)
