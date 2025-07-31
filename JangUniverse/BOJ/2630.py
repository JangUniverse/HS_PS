import sys
input = sys.stdin.readline

def cut(x, y, n):
    global w
    global b
    color = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != paper[i][j]:
                cut(x, y, n//2)
                cut(x, y+n//2, n//2)
                cut(x+n//2, y, n//2)
                cut(x+n//2, y+n//2, n//2)
                return
            
    if color == 0:
        w += 1
    else:
        b += 1

n = int(input())
paper = [list(map(int, input().split())) for i in range(n)]
w, b = 0, 0
cut(0, 0, n)
print(w)
print(b)