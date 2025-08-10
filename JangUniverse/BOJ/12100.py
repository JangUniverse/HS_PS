import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
res = 0

def move_up(li):
    new_board = [[0] * n for _ in range(n)]
    
    for c in range(n):
        idx = 0
        prev = -1
        merged = False
        
        for r in range(n):
            if li[r][c] != 0:
                if not merged:
                    prev = li[r][c]
                    merged = True
                else:
                    if li[r][c] == prev:
                        new_board[idx][c] = prev * 2
                        prev = -1
                        merged = False
                        idx += 1
                    else:
                        new_board[idx][c] = prev
                        prev = li[r][c]
                        idx += 1
        
        if prev != -1:
            new_board[idx][c] = prev
    
    return new_board

def move_down(li):
    new_board = [[0] * n for _ in range(n)]
    
    for c in range(n):
        idx = n - 1
        prev = -1
        merged = False
        
        for r in range(n - 1, -1, -1):
            if li[r][c] != 0:
                if not merged:
                    prev = li[r][c]
                    merged = True
                else:
                    if li[r][c] == prev:
                        new_board[idx][c] = prev * 2
                        prev = -1
                        merged = False
                        idx -= 1
                    else:
                        new_board[idx][c] = prev
                        prev = li[r][c]
                        idx -= 1
        
        if prev != -1:
            new_board[idx][c] = prev
    
    return new_board

def move_left(li):
    new_board = [[0] * n for _ in range(n)]
    
    for r in range(n):
        idx = 0
        prev = -1
        merged = False
        
        for c in range(n):
            if li[r][c] != 0:
                if not merged:
                    prev = li[r][c]
                    merged = True
                else:
                    if li[r][c] == prev:
                        new_board[r][idx] = prev * 2
                        prev = -1
                        merged = False
                        idx += 1
                    else:
                        new_board[r][idx] = prev
                        prev = li[r][c]
                        idx += 1
        
        if prev != -1:
            new_board[r][idx] = prev
    
    return new_board

def move_right(li):
    new_board = [[0] * n for _ in range(n)]
    
    for r in range(n):
        idx = n - 1
        prev = -1
        merged = False
        
        for c in range(n - 1, -1, -1):
            if li[r][c] != 0:
                if not merged:
                    prev = li[r][c]
                    merged = True
                else:
                    if li[r][c] == prev:
                        new_board[r][idx] = prev * 2
                        prev = -1
                        merged = False
                        idx -= 1
                    else:
                        new_board[r][idx] = prev
                        prev = li[r][c]
                        idx -= 1
        
        if prev != -1:
            new_board[r][idx] = prev
    
    return new_board

def dfs(li, cnt):
    global res
    
    if cnt == 5:
        for i in range(n):
            for j in range(n):
                res = max(res, li[i][j])
        return
    
    # 4방향으로 이동
    dfs(move_up(li), cnt + 1)
    dfs(move_down(li), cnt + 1)
    dfs(move_left(li), cnt + 1)
    dfs(move_right(li), cnt + 1)

dfs(board, 0)
print(res)