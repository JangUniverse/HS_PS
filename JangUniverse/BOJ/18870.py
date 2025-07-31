import sys
input = sys.stdin.readline

n = int(input())
c = list(map(int, input().split()))
c_sort = sorted(set(c))
d = {}
for i in range(len(c_sort)):
    d[c_sort[i]] = i
for j in c:
    print(d[j], end = " ")