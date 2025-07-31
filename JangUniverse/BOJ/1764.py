import sys
input = sys.stdin.readline

n, m = map(int, input().split())
list_n = set(input().rstrip() for _ in range(n))
list_m = [input().rstrip() for _ in range(m)]

res = []

for word in list_m:
    if word in list_n:
        res.append(word)

res.sort()
print(len(res))
print('\n'.join(res))
