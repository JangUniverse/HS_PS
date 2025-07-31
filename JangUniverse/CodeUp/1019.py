n = int(input())
a = n//10
b = n%10
x = 2*(b*10+a) % 100
if x <= 50:
    print(x)
    print('GOOD')
else:
    print(x)
    print('OH MY GOD')