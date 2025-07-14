a,b= input().split()
a=int(a)
b=int(b)
A=list()

for i in range(b):
    k=str(i)
    x=i
    for j in range(len(k)):
        x+=int(k[j])
    A.append(x)
s=0
for i in range(a,b):
    if A.count(i)==0:
        s+=i
print(s)