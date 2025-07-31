import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))
li.sort()

tmp = 0
res= 0
for i in li:
    tmp += i
    res += tmp
print(res)
