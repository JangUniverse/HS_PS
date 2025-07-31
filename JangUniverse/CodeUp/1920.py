def dec2bin(n):
    if n == 0:
        return '0'
    if n == 1:
        return '1'
    if n%2 == 0:
        return dec2bin(n//2)+'0'
    else:
        return dec2bin(n//2)+'1'

n = int(input())
print(dec2bin(n))