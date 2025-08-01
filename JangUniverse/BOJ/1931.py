import sys
input = sys.stdin.readline

n = int(input())
li = []
for i in range(n):
    x, y = map(int, input().split())
    li.append((x, y))
li.sort(key = lambda x: (x[1], x[0]))#처음보는 문법

cnt = 0
tmp = 0#현재시각

for s, e in li:
    if tmp <= s:
        tmp = e
        cnt+=1
print(cnt)