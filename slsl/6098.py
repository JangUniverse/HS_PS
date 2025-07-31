A=list()
for i in range(10):
    B=input().split()
    B.append(3)
    A.append(B)
A.append([3]*10)

i=1
j=1
while True:
    if A[i][j]=='2':
        A[i][j]=9
        break
    
    A[i][j]=9
    if (A[i+1][j]=='1' or A[i+1][j]==3) and (A[i][j+1]=='1' or A[i][j+1]==3):
        break

    elif A[i][j+1]=='1' or A[i][j+1]==3:
        i+=1
        continue
    else:
        j+=1
for i in range(10):
    for j in range(10):
        print(A[i][j],end=" ")
    print()