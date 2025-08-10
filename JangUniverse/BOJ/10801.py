a = list(map(int, input().split()))
b = list(map(int, input().split()))
cnta = 0
cntb = 0
for x, y in zip(a, b):
    if x>y:
        cnta += 1
    elif y>x:
        cntb += 1

if cnta > cntb:
    print('A')
elif cntb > cnta:
    print('B')
else:
    print('D')
