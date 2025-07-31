import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n, k = map(int, input().split())

def f(m, cnt):
    if cnt <= 0 and m > 0:
        return 0
    if m == 1:
        return 1
    elif m == 2:
        if cnt == 1:
            return 1
        else:
            return 2
    else:
        return f(m - 1, cnt - 1) + f(m - 2, cnt - 1)

print(f(n, k - 1))