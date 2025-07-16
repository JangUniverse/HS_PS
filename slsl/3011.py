n=int(input())
A=list(map(int,input().split()))
k=0
a=-1
while a!=k:
    x=False  
    a=k
    for i in range(n-1):
        if A[i]>A[i+1]:
            A[i],A[i+1]=A[i+1],A[i]
            x=True
    if x:
        k+=1
print(k)