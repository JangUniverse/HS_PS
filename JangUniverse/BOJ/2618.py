import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
w = int(input())
li = [[1, 1], [n,n]]
for i in range(w):
    li.append(list(map(int, input().split())))
dp = [[-1] * 1002 for _ in range(1002)]
dp_retrace = [[-1] * 1002 for _ in range(1002)]

def f(m, n):#걍 2항연산자
    return abs(li[m][0]-li[n][0])+abs(li[m][1]-li[n][1])

def police(m,n):
    nxt = max(m, n) +1
    

    if nxt == w + 2: #다음일이 없어
        return 0 
    
    if dp[m][n] != -1:
        return dp[m][n]
    
    c1 = police(nxt, n) + f(m, nxt)
    c2 = police(m, nxt) + f(n, nxt)

    if c1<c2:
        dp_retrace[m][n] =1
        dp[m][n] = c1
    else: 
        dp_retrace[m][n] =2
        dp[m][n] = c2
    
    return dp[m][n]

print(police(0,1))
m, n = 0, 1
for i in range(2, w+2):
    print(dp_retrace[m][n])
    if dp_retrace[m][n] == 1:
        m = i
    else:
        n = i