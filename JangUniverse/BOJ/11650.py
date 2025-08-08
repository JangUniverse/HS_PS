import sys
input = sys.stdin.readline
n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]
li = sorted(li, key = lambda x:(x[0], x[1]))
for x, y in li:
    print(x, y)