n=int(input())
A=input().split()
B=list()
for i in range(len(A)):
    B.append(int(A[i]))
B.sort()
B.reverse()
for i in range(len(B)):
    print(B[i],end=" ")
