import sys
input = sys.stdin.readline

n = int(input())
flag = False
c = 1
res = []
stack = []

for i in range(n):
    num = int(input())
    
    while c <= num:
        stack.append(c)
        res.append('+')
        c += 1
    
    if stack and stack[-1] == num:
        stack.pop()
        res.append('-')
    else:
        print("NO")
        flag = True
        break

if not flag:
    for op in res:
        print(op)