n = int(input())
li = list(map(int, input().split()))
res = []
for i in range(0, len(li), 2):
    res.append(max(li[i], li[i+1]))
print(*res)