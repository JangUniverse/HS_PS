A=input().split()
B=input().split()
c=A.pop()
k=0
for i in range(len(B)):
    if B[i] in A:
        k+=1
if k==6:
    print(1)
elif k==4:
    print(4)
elif k==3:
    print(5)
elif k==5:
    if c in B:
        print(2)
    else:
        print(3)
else:
    print(0)