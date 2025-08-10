import sys
input = sys.stdin.readline

n = int(input())
p = [0]
s = [0] *(n+1)

for i in range(n):
    a, b = map(int, input().split())
    p.append(a-b)

for j in range(1, n+1):
    s[j] = s[j-1] + p[j]

for i in s[1:]:
    print(i)