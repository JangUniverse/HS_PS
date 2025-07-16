n=int(input())
A=input().split()
for i in range(n):
    A[i]=int(A[i])
B=list()

for i in range(100001):
    B.append(0)

for i in range(n):
    k=A[i]
    B[k]+=1

for i in range(100001):
    if B[i]!=0:
        for j in range(B[i]):
            print(i,end=" ")
