n=int(input())
A=list(map(int,input().split()))
A.sort(key=lambda x: abs(x))
k=(abs(A[0]+A[1]),0,1)
for i in range(n-1):
    if k[0]>abs(A[i]+A[i+1]):
        k=(abs(A[i]+A[i+1]),i,i+1)
print(A[k[1]],A[k[2]])
