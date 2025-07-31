a,b=map(int,input().split())

if b in (1,3,5,7,8,10,12):
        print(31)
elif b==2:
    if a%400==0 or (a%4==0 and a%100!=0):
         print(29)
    else:
         print(28)
else:
    print(30)