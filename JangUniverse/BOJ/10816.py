import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

n = int(input())
li = sorted(list(map(int, input().split()))) 
m = int(input())
x = list(map(int, input().split()))

def count(li, x):
    l = bisect_left(li, x)
    r = bisect_right(li, x)
    return r - l

result = []
for i in x:
    result.append(count(li, i))

print(*result)