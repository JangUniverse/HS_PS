import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(input()))

stree = [0] * (4 * n) 
def init(s, e, idx):
    if s == e:
        stree[idx] = arr[s]
        return stree[idx]
    mid = (s + e) // 2
    stree[idx] = init(s, mid, idx * 2) + init(mid + 1, e, idx * 2 + 1)
    return stree[idx]

init(0, n - 1, 1)

def interval_sum(s, e, idx, l, r):
    if l > e or r < s:
        return 0
    if l <= s and r >= e:
        return stree[idx]
    mid = (s + e) // 2
    return interval_sum(s, mid, idx * 2, l, r) + interval_sum(mid + 1, e, idx * 2 + 1, l, r)

def update(s, e, idx, a, v):
    if a < s or a > e:
        return
    stree[idx] += v
    if s == e:
        return
    mid = (s + e) // 2
    update(s, mid, idx * 2, a, v)
    update(mid + 1, e, idx * 2 + 1, a, v)

for i in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        b -= 1
        diff = c - arr[b]
        arr[b] = c
        update(0, n - 1, 1, b, diff)
    elif a == 2:
        print(interval_sum(0, n - 1, 1, b - 1, c - 1))