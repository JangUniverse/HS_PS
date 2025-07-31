n=int(input())
k=n
s=int(input())
A=input().split()
for i in range(s):
    n=n*((100+int(A[i]))/100)
print(round(n-k))
if k-n>0:
    print('bad')
elif k-n==0:
    print('same')
else:
    print('good')