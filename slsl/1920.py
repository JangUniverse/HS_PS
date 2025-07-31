def f(n):
    if n//2==0 and n%2==0:
        return str(0)
    return f(n//2)+str(n%2)
n=int(input())
if n==0:
    print(0)
else:
    print(f(n)[1:])