a,b=map(int,input().split())
k=a+b
if k<a-b:
    k=a-b
if k<b-a:
    k=b-a
if k<a*b:
    k=a*b
if k<a/b:
    k=a/b
if k<b/a:
    k=b/a
if k<a**b:
    k=a**b
if k<b**a:
    k=b**a
print(format(k,".6f"))