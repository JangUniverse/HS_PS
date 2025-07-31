n = int(input())
flag = 0
for i in range(2, int(n**(1/2))+2):
    if n == 2:
        flag = 0
        break
    if n % i == 0:
        flag = 1
        break
    else:
        continue
if flag == 0:
    print('prime')
else:
    print('composite')