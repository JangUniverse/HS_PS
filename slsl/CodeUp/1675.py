syzer=input()
A=list()
B=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in range(len(syzer)):
    A.append(syzer[i])

for i in range(len(A)):
    if A[i]=='a':
        A[i]='x'
    elif A[i]=='b':
        A[i]='y'
    elif A[i]=='c':
        A[i]='z'
    elif A[i]==' ':
        continue
    else:
        P=B.index(A[i])
        A[i]=B[P-3]
for i in range(len(A)):
    print(A[i],end="")