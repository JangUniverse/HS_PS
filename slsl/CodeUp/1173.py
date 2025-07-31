a,b=map(int,input().split())
if b>=30:
    print(a,b-30)
else:
    if a==0:
        print(23,b+30)
    else:
        print(a-1,b+30)