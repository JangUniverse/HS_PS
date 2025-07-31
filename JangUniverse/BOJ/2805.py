import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tree = list(map(int, input().split()))
tree.sort()
s, e = 1, tree[-1]

while s <= e:
    mid = (s + e) // 2
    cnt = 0
    for i in range(n-1, -1, -1):
        if mid > tree[i]:
            break
        else:
            cnt += tree[i] - mid
    
    if cnt >= m:
        s = mid + 1
    else:
        e = mid - 1

print(e)