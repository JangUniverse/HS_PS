import sys
inf = float('inf')
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))
#이분탐색 문제
ans = [inf, inf]
l, r = 0, n-1#two pointers
minimum = inf

while l<r:
    if abs(li[l]+li[r]) < minimum:
        minimum = abs(li[l]+li[r])
        ans = [li[l], li[r]]

    if li[l] + li[r] < 0:#강염기
        l += 1
    else: #강산
        r -= 1

print(*ans)
