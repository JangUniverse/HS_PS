def wu(n):
    if n == 1:
        return
    if n % 2 == 1:
        n = 3 * n + 1
    else:
        n = n // 2 
    print(n)
    return wu(n)

n = int(input())
print(n)
wu(n)
