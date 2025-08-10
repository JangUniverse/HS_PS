import sys
input = sys.stdin.readline

s, x = 0, 0
m = int(input().rstrip())
for _ in range(m):
    o = list(map(int, input().rstrip().split()))
    if o[0] == 1:
        s += o[1]
        x ^= o[1]
    elif o[0] == 2:
        s -= o[1]
        x ^= o[1]
    elif o[0] == 3:
        print(s)
    elif o[0] == 4:
        print(x)