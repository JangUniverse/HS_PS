n=int(input())
A=list(map(int,input().split()))
B=list()
C=list()
for i in range(n):
    C.append(0)
for i in range(n):
    B.append([i,A[i]])
B.sort(key=lambda x: x[1])

for i in range(n):
        C[B[i][0]]=i
for i in range(n):
    print(C[i],end=" ")