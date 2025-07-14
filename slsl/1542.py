n=int(input())
for i in range(1,int(n**(1/2))+1):
    if n//i==0:
        k=1
        print(i)
        break
    k=0
if k:
    print("composite")
else:
    print("prime")