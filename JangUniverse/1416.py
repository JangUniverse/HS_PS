n = int(input())

if n == 0:
    print(0)
else:
    bits = []
    while n > 0:
        bits.append(str(n % 2)) 
        n //= 2
    print(''.join(reversed(bits)))