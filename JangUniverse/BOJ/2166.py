#성두썜이랑 배웠던걸로 날먹할 수 있음
import sys
input = sys.stdin.readline

n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]
li.append(li[0])
ans = 0

for i in range(n):
    ans += li[i][0] * li[i+1][1] - li[i+1][0]*li[i][1]
print(round(abs(ans)/2,1))