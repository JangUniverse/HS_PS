n=int(input())
A=input().split()
a,b=input().split()
x=int(A[int(a)-1])
k=int(a)
for i in range(int(a)-1,int(b)):
    if x<int(A[i]):
        k=int(i+1)
        x=int(A[i])
print(k)
