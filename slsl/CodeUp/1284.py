n=int(input())
A=list()
for i in range(2,n):
    if n%i==0:
        A.append(i)
if len(A)==2 and (n//A[0])//A[1]==1 and not A[1]%A[0]==0:
    print(A[0],A[1])
else:
    print('wrong number')