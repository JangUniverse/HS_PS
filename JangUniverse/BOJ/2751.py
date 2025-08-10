import sys
input = sys.stdin.readline
n = int(input())
li = list(int(input()) for  _ in range(n))
li = list(set(li))
li.sort()
for i in li:
    print(i)
    