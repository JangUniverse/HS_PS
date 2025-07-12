s, e, x = map(int, input().split())
if e > x:
    e, x = x, e
if s > e:
    s, e = e, s
if e > x:
    e, x = x, e
print(e)