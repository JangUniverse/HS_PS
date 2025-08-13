
import bisect

n = int(input())
a = list(map(int, input().split()))

cnt = 0
processed = []
for i in range(n - 1, -1, -1): 
    pos = bisect.bisect_left(processed, a[i])
    cnt += pos
    bisect.insort(processed, a[i])

print(cnt)