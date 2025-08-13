#이분탐색
import sys
input = sys.stdin.readline
import bisect

def place(p, m, dist):
    #dist 유지하면서 M개 배치 ㄱㄴ?
    cnt = 1
    last  = p[0]

    for i in range(1, len(p)):
        if p[i] - last >= dist:
            cnt +=1
            last  = p[i]
            
            if  cnt >= m:
                return True
    return False


n, m = map(int, input().split())
pos = list(int(input()) for _ in range(n))
pos.sort()
l, r = 1, pos[-1]-pos[0]
ans = 0

while l <= r:
    mid =  (l+r)//2
    if place(pos, m, mid):
        ans = mid
        l = mid + 1
    else:
        r = mid -1

print(ans)