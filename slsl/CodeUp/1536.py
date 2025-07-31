n=int(input())
A=input().split()
x=int(A[0])
for i in range(n):
    if x>int(A[i]):
        x=int(A[i])
print(x)
