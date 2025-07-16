a, b = map(str, input().split())
count = 0
if len(a) > len(b):
    print(b,a)
elif len(b) > len(a):
    print(a,b)

else:
    for i in range(len(a)):
        x, y  = a[i], b[i]
        if y>x:
            print(a, b)
            break
        elif x>y:
            print(b, a)
            break
        else:
            count += 1
if count == len(a):
    print(b,a)