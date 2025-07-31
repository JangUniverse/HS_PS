a, b = map(float, input().split())
while True:
    if a > b:
        break
    print(f"{a:.2f}", end = ' ')
    a = a+0.01