import sys
input = sys.stdin.readline

M = int(input())
s = set()

for i in range(M):
    i = input().rstrip().split()
    if len(i) == 1:
        if i[0] == 'all':
            s = set([k for k in range(1, 21)])
        else:
            s = set()
        continue
    if i[0] == 'add':
        s.add(int(i[1]))
    elif i[0] == 'remove':
        s.discard(int(i[1]))
    elif i[0] == 'check':
        if int(i[1]) in s:
            print(1)
        else:
            print(0)
    elif i[0] == "toggle":
        if int(i[1]) in s:
            s.discard(int(i[1]))
        else:
            s.add(int(i[1]))