import sys
input = sys.stdin.readline
n, m , k, x, y = map(int, input().split())
li = list()
for i in range(n):
    a, b = map(int, input().split())
    c = a*x - b*y
    li.append(c)
li.sort()
basetime = k * (x+y)
total = sum(li[:m])
print(basetime + total)
