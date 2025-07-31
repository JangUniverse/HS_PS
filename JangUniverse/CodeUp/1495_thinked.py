import sys
input = sys.stdin.readline

k, m, n = map(int, input().split())

d = [[0] * 1001 for _ in range(1001)]
arr = [[0] * 1001 for _ in range(1001)]

for _ in range(n):
    x1, y1, x2, y2, u = map(int, input().split())
    d[x1][y1] += u
    d[x2 + 1][y2 + 1] += u
    d[x1][y2 + 1] -= u
    d[x2 + 1][y1] -= u

for i in range(k):
    for j in range(m):
        print(d[i][j], end=' ')
    print()
print()

# 시간 단축을 위해 조건문 사용
# 자신의 왼쪽과 위를 더한 거에 i-1, j-1을 빼면 중복된 부분이 제거됨
for i in range(k):
    for j in range(m):
        if not i and not j:
            arr[i][j] = d[i][j]
        elif not i:
            arr[i][j] = arr[i][j - 1] + d[i][j]
        elif not j:
            arr[i][j] = arr[i - 1][j] + d[i][j]
        else:
            arr[i][j] = arr[i][j - 1] + arr[i - 1][j] - arr[i - 1][j - 1] + d[i][j]
        print(arr[i][j], end=' ')
    print()