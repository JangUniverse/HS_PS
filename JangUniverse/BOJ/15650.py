import sys
input = sys.stdin.readline
def dfs(now):
    if len(num) == m:
        print(*num)
        return
    for i in range(now, n+1):
        if i not in num:
            num.append(i)
            dfs(i+1)
            num.pop()#pruning
n, m = map(int, input().split())
num = list()
dfs(1)