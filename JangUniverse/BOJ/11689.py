import sys
input = sys.stdin.readline

def euler_phi(n):
    res = n
    cnt = 2
    while cnt * cnt <= n:
        if n % cnt == 0:
            while n % cnt == 0:
                n //= cnt
            res = res - res // cnt
        cnt += 1
    
    if n > 1:
        res = res - res // n
    return res
n = int(input())
print(euler_phi(n))