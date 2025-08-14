import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

ans = 0
cur = 0
f = -2

for i in range(n):
    if arr[i]:
        cur += 1
    elif i - f >= 2:
        f = i
    else:
        cur = 0
    ans = max(ans, cur)

print(ans)