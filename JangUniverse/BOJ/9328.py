import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

t = int(input())

def move(y, x):
    global h, w, cnt
    if not 0 <= y < h:
        return
    if not 0 <= x < w:
        return
    if visited[y][x] == 1:
        return
    n = ord(li[y][x])
    if n == 42:  # '*'
        return
    elif 65 <= n <= 90:  # 대문자 (문)
        door[li[y][x]].append([y, x])
        return
    elif 97 <= n <= 122:  # 소문자 (열쇠)
        find.append(li[y][x])
    elif n == 36:  # '$'
        cnt += 1
    
    visited[y][x] = 1
    move(y-1, x)
    move(y+1, x)
    move(y, x-1)
    move(y, x+1)

for _ in range(t):
    h, w = map(int, input().split())
    li = [input().rstrip() for _ in range(h)]
    visited = [[0] * w for _ in range(h)]
    door = defaultdict(list)
    find = []
    cnt = 0
    
    keys = input().rstrip()
    for key in keys:
        if key != '0':
            for i in range(h):
                li[i] = li[i].replace(key.upper(), '.')
    
    for i in range(h):
        move(i, 0)
        move(i, w-1)
    for i in range(w):
        move(0, i)
        move(h-1, i)
    
    while find:
        key = find.pop()
        for i in range(h):
            li[i] = li[i].replace(key.upper(), '.')
        for y, x in door[key.upper()]:
            move(y, x)
    
    print(cnt)