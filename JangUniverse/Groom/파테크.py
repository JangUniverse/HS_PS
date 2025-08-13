N, M = map(int, input().split())
onions = list(map(int, input().split()))

l, r = 0, max(onions)
ans = 0
while l <= r:
    mid = (l + r) // 2
    total = sum(o - mid for o in onions if o > mid)
    if total >= M:
        ans = mid
        l = mid + 1
    else:          
        r = mid - 1

print(ans)
