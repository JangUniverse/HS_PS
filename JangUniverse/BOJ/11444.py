import sys
from collections import  defaultdict
input = sys.stdin.readline
mod = 1000000007
memo = defaultdict(int)
memo[1], memo[2] = 1, 1
#행렬식은 쎄벼옴 
def fibo(n):
    if n in memo:
        return memo[n]
    
    if n % 2 == 0:  
        k = n // 2
        fk = fibo(k)
        fk_1 = fibo(k - 1)
        memo[n] = (fk * (2 * fk_1 + fk)) % mod
    else:  # n이 홀수
        k = (n + 1) // 2
        fk = fibo(k)
        fk_1 = fibo(k - 1)
        memo[n] = (fk * fk + fk_1 * fk_1) % mod
    
    return memo[n]
    
n = int(input())
print(fibo(n))