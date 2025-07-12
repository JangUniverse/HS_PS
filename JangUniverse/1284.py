def prime(x):
    if x<2:
        return False
    for i in range(2, int(x**(1/2))+1):
        if x % i == 0:
            return False
    return True
flag = 0    
n = int(input())
for i in range(2, int(n**(1/2))+1):
    if n%i == 0:
        j = n//i
        if prime(i) and prime(j) == True:
            print(min(i, j), max(i, j))
            flag = 1
            break
        
if flag == 0:
    print("wrong number")