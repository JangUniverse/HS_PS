n = int(input())
li = list(map(int, input().split()))
cnt = [0]*500001

for i in range(n):
    num = li[i]
    cnt[num] += 1
for j in range(len(cnt)-1):
    cnt[j+1] += cnt[j]
for k in li:
    print(cnt[k]-1, end =' ')