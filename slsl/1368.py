a,b,c=input().split()
if c=='L':
    for i in range(int(a)):
        for _ in range(i):
            print(end=' ')
        print('*'*int(b))
else:
    for i in range(int(a)-1,-1,-1):
        for _ in range(i):
            print(end=' ')
        print('*'*int(b))