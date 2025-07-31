n = int(input())
li = list(map(int, input().split()))
x = int(input())
res = -1
for i in range(n):
    if li[i] >= x:
        res = i+1
        print(i+1)
        break
if res == -1:
    print(n+1)