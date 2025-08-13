import sys
input =sys.stdin.readline
n = int(input())
mod = 10**9+7

if n == 1:
    print(1)
else:
    res = 1
    base = 2
    exp = n-2
    while exp > 0:
        if exp & 1:
            res = (res * base) % mod
        base *= base %mod
        exp >>= 1
    print(res)