s, e= map(int, input().split())
flag = 0
a = [1, 3, 5, 7, 8, 10, 12]
if (s % 4 == 0 and s % 100 == 0 and s % 400 == 0) or (s % 4 == 0 and s % 100 !=  0):
    flag = 1
if e == 2:
    if flag == 1:
        print(29)
    else:
        print(28)
elif e in a:
    print(31)
else:
    print(30)