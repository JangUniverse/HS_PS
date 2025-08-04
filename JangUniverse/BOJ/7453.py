import sys
input = sys.stdin.readline

n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]

#리스트 병합문제
ab, cd = [], []
for i in range(n):
    for j in range(n):
        ab.append(li[i][0] + li[j][1])
        cd.append(li[i][2] + li[j][3])

ab.sort()
cd.sort(reverse=True)

p1, p2 = 0, 0
length = n **2 
res = 0

while p1 < length and p2 < length:
    v1, v2 = ab[p1], cd[p2]
    
    if v1 + v2 == 0:
        cnt1, cnt2 = 0, 0
        
        while p1 < length and ab[p1] == v1:
            p1 += 1
            cnt1 += 1
        while p2 < length and cd[p2] == v2:
            p2 += 1
            cnt2 += 1
            
        res += cnt1 * cnt2
        
    elif v1 + v2 > 0:
        p2 += 1
    else:
        p1 += 1

print(res)