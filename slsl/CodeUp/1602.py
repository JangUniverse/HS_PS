def f(n):
    if n<0:
        return -n
    else:
        return n
n=float(input())
if n==int(n):
    n=int(n)
print(f(n))
