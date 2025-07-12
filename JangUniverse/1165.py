s, e = map(int, input().split())
while True:
    if s >= 90:
        break
    s += 5
    e += 1
print(e)