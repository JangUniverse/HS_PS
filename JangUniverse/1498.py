n, g = map(int, input().split())
li = list(map(int, input().split()))

if n%g == 0:
    for i in range(n//g):
        res = sorted(li[i*g:((i+1)*g)])
        print(res[0], end = ' ')
else:
    for i in range(n//g+1):
        if ((i+1)*g > n):
            res = sorted(li[i*g:])
        else:
            res = sorted(li[i*g:((i+1)*g)])
        print(res[0], end = ' ')