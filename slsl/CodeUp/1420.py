n=int(input())
A=dict()
for i in range(n):
    a,b=input().split()
    A[a]=int(b)
B=sorted(A.values())
for key in A.keys():
    if A[key]==B[-3]:
        print(key)
