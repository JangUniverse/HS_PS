import sys
input =sys.stdin.readline
inf = float('inf')

n = int(input())
li = list(map(int, input()).split())
li.sort()
minimum = inf
res = list()
for i in range(n-2):
    s = i+1
    e = n-1

    while s<e:
        tmp = li[i] + li[s] +li[e]
        if abs(tmp) < minimum:
            minimum = abs(tmp)
            res = [li[i], li[s], li[e]]
        
        if tmp < 0:
            s += 1
        elif tmp > 0:
            e -= 1
        else:
            break
print(*res) 