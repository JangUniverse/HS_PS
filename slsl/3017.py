n=int(input())
A=list()
for i in range(n):
    k=list(map(int,input().split()))
    k.append(i+1)
    A.append(k)

for i in range(n):
    for j in range(i+1,n):
        if A[i][0]<A[j][0]:
            A[i],A[j]=A[j],A[i]
        elif A[i][0]==A[j][0]:
            if A[i][1]<A[j][1]:
                A[i],A[j]=A[j],A[i]
            elif A[i][1]==A[j][1]:
                if A[i][2]>A[j][2]:
                    A[i],A[j]=A[j],A[i]
for i in range(n):
    print(A[i][2],A[i][0],A[i][1])

# n=int(input())
# A=list()
# for i in range(n):
#     k=list(map(int,input().split()))
#     k.append(i+1)
#     A.append(k)
# A.sort(key=lambda x: (x[0], x[1], -x[2]), reverse=True)
# for i in range(n):
#     print(A[i][2],A[i][0],A[i][1])