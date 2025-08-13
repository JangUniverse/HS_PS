import sys
input =sys.stdin.readline
n = int(input())
li = list()

for _ in range(n):
    c, a =  input().split()

    if c =='add':
        li.append(a)
    elif c == 'find':
        count = 0
        for i in li:
            if i.startswith(a):
                count += 1
        print(count)