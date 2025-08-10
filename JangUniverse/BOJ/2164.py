import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
s = 2

while 1:
    if n == 1 or n == 2:
        print(n)
        break
    s *= 2
    if s >= n:
        print((n-s//2)*2)
        break