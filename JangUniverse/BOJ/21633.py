import sys
input = sys.stdin.readline
n = int(input())
fee = 25 + n / 100
if fee < 100:
    fee = 100
elif fee > 2000:
    fee = 2000

print(f'{fee:.2f}')