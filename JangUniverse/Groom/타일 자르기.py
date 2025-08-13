K, N = map(int, input().split())
tiles = [int(input()) for _ in range(K)]

l, r = 1, max(tiles)
ans = 0
while l <= r:
    m = (l + r) // 2
    cnt = sum(t // m for t in tiles)
    if cnt >= N:
        ans = m
        l = m + 1
    else:
        r = m - 1

print(ans)
