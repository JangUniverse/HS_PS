n=int(input())
p=n//2
for i in range(p,-1,-1):
    for _ in range(i):
        print(end=" ")
    print("*"*(n-2*i))
    