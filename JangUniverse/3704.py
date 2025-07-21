import sys
sys.setrecursionlimit(10**6)
def f(n, a):
    if n == 1:
        a[n] = 1
        return 1
    if n == 2:
        a[n]= 2
        return 2
    if n == 3:
        a[n]= 4
        return  4
    if a[n]:
        return a[n]#memoization
    else:
        a[n] = (f(n-3, a)+f(n-2,a)+f(n-1,a))%1000
        return a[n]
    
n = int(input())
a = [0] *(n+1)
print(f(n,a))