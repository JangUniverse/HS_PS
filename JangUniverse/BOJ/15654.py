import sys
input = sys.stdin.readline

def dfs():
    if len(num) == m:
        print(*num)
        return
    
    prev = 0  
    for i in range(n):
        if not used[i] and arr[i] != prev:
            num.append(arr[i])
            used[i] = True
            prev = arr[i]
            dfs()
            used[i] = False
            num.pop()

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
used = [False] * n
num = []

dfs()