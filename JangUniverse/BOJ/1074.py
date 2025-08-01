#사분면을 나눠야하나
import sys
input = sys.stdin.readline
ans = 0
N, r, c= map(int, input().split())
while N != 0:
    N -= 1
    if r < 2**N and c >= 2**N:
        ans += (2**N) * (2**N)
        c -= (2**N)
    elif r<2**N and c < 2**N:
        ans += 0
    elif r>= 2**N and c <2**N:
        ans += (2**N) * (2**N)*2
        r-= 2**N
    else:
        ans += (2**N)*(2**N)*3
        r -= 2**N
        c -= 2**N
print(ans)