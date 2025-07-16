def d(n):
    generate_number = n
    while n > 0:
        generate_number += n % 10
        n //= 10
    return generate_number

a, b = map(int, input().split())
self_numbers = [i for i in range(b + 1)]

for i in range(1, b):
    res = d(i)
    if res <= b:
        self_numbers[res] = 0

answer = 0
for i in range(a, b + 1):
    if self_numbers[i] > 0:
        answer += self_numbers[i]

print(answer)