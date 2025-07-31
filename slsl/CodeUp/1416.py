n=int(input())
k=n
A=list()
while n>=1:
    A.append(n%2)
    n=n//2
if k==0:
    print(0)
else:
    for i in range(1,len(A)+1):
        print(A[-i],end="")