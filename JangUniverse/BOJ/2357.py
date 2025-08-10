import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
inf = float('inf')

def init(s, e, idx):
    if s == e:
        stree[idx] = [arr[s], arr[s]]
        return stree[idx]
    
    mid = (s+e)//2
    left = init(s, mid, idx*2)
    right = init(mid+1, e, idx*2+1)
    stree[idx] = [min(left[0], right[0]), max(left[1], right[1])] 
    return stree[idx]

def find(s, e, idx, l, r):
    if s > r or e < l:
        return [inf, 0]
    
    if l <= s and r >= e:
        return stree[idx]
    
    mid = (s+e)//2
    left = find(s, mid, idx*2, l, r)
    right = find(mid+1, e, idx*2+1, l, r)
    return [min(left[0], right[0]), max(left[1], right[1])] 

n, m = map(int, input().split())
arr = []
stree = [0] * (4*n)
ans = []

for _ in range(n):
    arr.append(int(input()))

init(0, n-1, 1)

for i in range(m):
    a, b = map(int, input().split())
    ans.append(find(0, n-1, 1, a-1, b-1))

for x in ans:
    print(*x)