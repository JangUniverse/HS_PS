h, k, d = map(str, input().split())
h = int(h)
k = int(k)

if d == 'L':
    for i in range(h):
        print(' ' * i + '*' * k)
elif d == 'R':
    for i in range(h):
        print(' ' * (h - 1 - i) + '*' * k)
