a,b=input().split()
A=(int(a),int(b))

def f(n,m):
    if n==1:
        return 1,1
    elif m==1:
        return 1,1
    elif n<m:
        return n,m%n
    else:
        return n%m,m
    
while A[0]!=A[1]:
    A=f(A[0],A[1])
    if A[0]==0:
        A=(A[1],A[1])
    elif A[1]==0:
        A=(A[0],A[0])
k=A[0]
print(int(a)*int(b)//k)    
