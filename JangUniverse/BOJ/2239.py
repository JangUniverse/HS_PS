import sys
input = sys.stdin.readline

li = [list(map(int, input().rstrip())) for _ in range(9)]
zero_idx = []
for r in range(9):
    for c in range(9):
        if li[r][c] == 0:
            zero_idx.append((r, c))

def rowcheck(r, n):
    for c in range(9):
        if li[r][c] == n:
            return False
    return True

def colcheck(c, n):
    for r in range(9): 
        if li[r][c] == n:
            return False
    return True

def squarecheck(r, c, n):
    r, c = r // 3 * 3, c // 3 * 3 
    for i in range(3):
        for j in range(3):
            if li[r+i][c+j] == n:
                return False
    return True

def dfs(idx):
    if idx == len(zero_idx): 
        for r in li:
            print(''.join(map(str, r)))
        return True  
    
    y, x = zero_idx[idx]

    for i in range(1, 10): 
        if rowcheck(y, i) and colcheck(x, i) and squarecheck(y, x, i):
            li[y][x] = i
            if dfs(idx+1): 
                return True
            li[y][x] = 0
    
    return False 

dfs(0)