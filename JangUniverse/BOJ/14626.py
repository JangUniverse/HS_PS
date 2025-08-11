import sys
input = sys.stdin.readline
isbn = input()
res = 0
even = False

for i in range(13):
    if isbn[i] == '*':
        if i%2 != 0:
            even = True
        continue

    res += int(isbn[i]) * (1 if i%2 == 0 else 3)

if even:
    for i in range(10):
        if (res + 3*i) % 10 == 0:
            print(i)
            break
else:
    print(10- res%10)
    