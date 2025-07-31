a,b=map(int,input().split())
X=[[0]*b for _ in range(a)]

n=int(input())
for i in range(n):
    A=input().split()
    for k in range(len(A)):
        A[k]=int(A[k])

    if A[1]==1:
        for j in range(A[0]):
            X[A[2]-1+j][A[3]-1]=1

    if A[1]==0:
        for j in range(A[0]):
            X[A[2]-1][A[3]-1+j]=1
for i in range(a):
    for j in range(b):
        print(X[i][j],end=" ")
    print()