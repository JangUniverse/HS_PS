def pascal(r, c, a):
    if r == 1 or c == 1:
        a[r-1][c-1] = 1
        return 1

    if a[r-1][c-1]:
        return a[r-1][c-1]
    else:
        a[r-1][c-1] = pascal(r-1, c, a)+pascal(r, c-1, a)
        return a[r-1][c-1]

r, c=map(int, input().split())
a = [[0]*c for i in range(r)]
print(pascal(r, c, a)%100000000)