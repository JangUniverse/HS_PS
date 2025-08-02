n = int(input())
res = 0
row = [-1] * n

def nqueen(x):
    global res
    if x == n:
        res += 1
        return
    
    for i in range(n):
        for j in range(x):
            if row[j] == i: 
                break
            if x - j == abs(i - row[j]):  
                break
        else:  
            row[x] = i
            nqueen(x + 1)

nqueen(0)
print(res)