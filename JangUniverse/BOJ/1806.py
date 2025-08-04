import sys
input = sys.stdin.readline

n, s = map(int, input().split())
li = list(map(int, input().split()))

l, r = 0, 0
tmp = 0
ans = float('inf')

while r < n:
    tmp += li[r]
    
    while tmp >= s:
        ans = min(ans, r - l + 1)
        tmp -= li[l]
        l += 1
    
    r += 1

if ans == float('inf'):
    print(0)
else:
    print(ans)