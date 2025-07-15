n = int(input())
li = list([0] * n for _ in range(n))
count = 1
row, col = n-1, 0
direction = 1 #1 is up&right

for i in range(n, 0, -1): #length of each line(to upper)
    for j in range(i):
        li[row][col] =count
        count += 1

        if j == i-1: #last index
            if direction == 1:
                row += 1
            else:
                col += 1
        
        else:
            row -= direction
            col += direction
    
    direction *= -1

for i in range(n):
    print(*li[i])