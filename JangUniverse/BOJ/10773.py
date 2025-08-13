import sys
input = sys.stdin.readline

k = int(input())
stack = list()

for i in range(k):
    x = int(input())
    if x == 0:
        stack.pop()
    else:
        stack.append(x)

print(sum(stack))