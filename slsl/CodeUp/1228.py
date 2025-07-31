a,b=map(float,input().split())
standard=(a-100)*0.9
f=(b-standard)*100/standard
if f<=10:
    print('정상')
elif f>20:
    print('비만')
else:
    print('과체중')