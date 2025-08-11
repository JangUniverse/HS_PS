import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
li = []
li = [list(map(int, input().split())) for _ in range(n)]
q = int(input())
radiuses = [int(input()) for _ in range(q)]

in_sector = [] 
out_sector = 0  

for x, y in li:
    if y >= x and y >= -x:  #
        distance_sq = x * x + y * y
        in_sector.append(distance_sq)
    else: 
        out_sector += 1
in_sector.sort()

for r in radiuses:
    r_sq = r * r
    
    infield_count = bisect_left(in_sector, r_sq + 1)
    homerun_count = len(in_sector) - infield_count
    foul_count = out_sector
    
    print(foul_count, infield_count, homerun_count)