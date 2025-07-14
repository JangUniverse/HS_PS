n=int(input())
A=input().split()
k=int(input())
for i in range(n):
    if k<=int(A[i]):
        print(i+1)
        x=False
        break
    x=True
if x:
    print(n+1)