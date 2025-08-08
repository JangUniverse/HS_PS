import sys
input = sys.stdin.readline

n = int(input())
li = list()
for i in range(n):
    a, b = input().split()
    li.append((int(a), b))

li = sorted(li, key=lambda x:x[0])
for x, y in li:
    print(x,y)