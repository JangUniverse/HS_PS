import sys
input = sys.stdin.readline

n, m = map(int, input().split())
li= list(map(int, input().split()))
res = 0

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            tmp = li[i]+li[j]+li[k]
            
            if res <= tmp <= m:
                res = tmp
print(res)