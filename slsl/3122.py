n=int(input())
for i in range(n-1,0,-1):
    for k in range(i):
        print(end=" ")
    print("*"*(2*n-2*i-1),end="")
    for k in range(i):
        print(end=" ")
    print()
print("*"*(2*n-1))
for i in range(1,n):
    for k in range(i):
        print(end=" ")
    print("*"*(2*n-2*i-1),end="")
    for k in range(i):
        print(end=" ")
    print()