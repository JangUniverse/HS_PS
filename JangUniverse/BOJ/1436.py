import sys
input = sys.stdin.readline
n = int(input())
res = 0
cnt = 0
while cnt != n:
    if '666' in str(res):
        cnt += 1
    res += 1
print(res -1)