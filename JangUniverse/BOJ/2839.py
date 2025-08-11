import sys
input = sys.stdin.readline
n = int(input())
res = 0
while 1:
    if n % 5 != 0:
        n -= 3
        res += 1
    elif n % 5 == 0:
        res += n //5
        print(res)
        break
    if n < 0:
        print(-1)
        break