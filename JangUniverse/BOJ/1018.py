import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [input().strip() for _ in range(n)]

res = []

for i in range(n-7):
    for j in range(m-7):
        black_start = 0 
        white_start = 0 

        for row in range(i, i+8):
            for col in range(j, j+8):
                if (row + col) % 2 == 0: 
                    if board[row][col] != 'B':
                        black_start += 1
                else: 
                    if board[row][col] != 'W':
                        black_start += 1

                if (row + col) % 2 == 0: 
                    if board[row][col] != 'W':
                        white_start += 1
                else: 
                    if board[row][col] != 'B':
                        white_start += 1
        res.append(black_start)
        res.append(white_start)

print(min(res))