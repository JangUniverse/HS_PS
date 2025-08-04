import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))
ans = 0
lis = list()

for i in  li:
    if not lis:
        lis.append(i)
        ans += 1
    if lis[-1] < i:
        lis.append(i)
        ans += 1
    else:
        idx = bisect_left(lis, i)
        lis[idx] = i

print(ans)
