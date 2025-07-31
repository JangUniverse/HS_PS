a = int(input())
b = int(input())
c = list(map(int, input().split()))
x = a
for i in range(b):
    x *= (1+c[i]/100)
print(round(x-a))
if round(x, 0) > a:
    print('good')
elif round(x, 0) == a:
    print('same')
else:
    print('bad')