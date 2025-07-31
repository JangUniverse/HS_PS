k=input()
if '+' in k:
    a,b=k.split('+')
    a,b=int(a),int(b)
    print(a+b)
if '-' in k:
    a,b=k.split('-')
    a,b=int(a),int(b)
    print(a-b)
if '*' in k:
    a,b=k.split('*')
    a,b=int(a),int(b)
    print(a*b)
if '/' in k:
    a,b=k.split('/')
    a,b=int(a),int(b)
    print(format(a/b,".2f"))