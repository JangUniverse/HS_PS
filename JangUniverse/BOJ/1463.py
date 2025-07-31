#3으로 나누어떨어진 --> /3 or -1
#2로 나누어떨어짐 --> -1 or /2
#else -1

import sys
input = sys.stdin.readline

n = int(input())
d = [0] * 1000001

for i in range(2, n+1):
    d[i] = d[i-1] + 1 
    if i % 2 == 0: 
        d[i] = min(d[i], d[i//2] + 1) 

    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)

print(d[n])