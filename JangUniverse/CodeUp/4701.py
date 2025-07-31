n = int(input())
li = list(map(int, input().split()))
li.sort(key=abs)  # 절댓값 기준 정렬

min_sum = float('inf')
minA, minB = 100001, 100001

for i in range(n - 1):
    s = abs(li[i] + li[i + 1])
    if s < min_sum:
        min_sum = s
        minA = li[i]
        minB = li[i + 1]

# 오름차순 출력
if minA < minB:
    print(minA, minB)
else:
    print(minB, minA)
