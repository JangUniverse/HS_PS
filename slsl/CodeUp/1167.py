a,b,c=map(int,input().split())
if a-b>0 and a-c>0:
    if b-c>0:
        print(b)
    else:
        print(c)
elif b-c>0 and b-a>0:
    if a-c>0:
        print(a)
    else:
        print(c)
else:
    if a-b>0:
        print(a)
    else:
        print(b)