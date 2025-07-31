a,b=map(int,input().split())
for i in range(b):
    for j in range(a):
        for k in range(j):
            print(end=" ")
        print("*")

    for j in range(a,1,-1):
        for k in range(j-2):
            print(end=" ")
        print("*")