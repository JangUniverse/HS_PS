import sys
input = sys.stdin.readline
n = int(input())
if n % 2:
    print(0)
else:
    if n * (n + 1) // 2 % 2:
        print(1)
    else:
        print(2)