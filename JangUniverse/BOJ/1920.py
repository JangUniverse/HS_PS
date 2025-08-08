import sys
import bisect
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
m = int(input())
test = list(map(int, input().split()))
a.sort()

for i in test:
    if a[bisect.bisect(a, i)-1] == i:
        print(1)
    else:
        print(0)