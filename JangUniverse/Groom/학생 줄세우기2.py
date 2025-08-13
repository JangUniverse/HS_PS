import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
sorted_arr = sorted([(val, idx) for idx, val in enumerate(arr)])
visited = [0] * N
ans = 0

for i in range(N):
    if visited[i] or sorted_arr[i][1] == i:
        continue
    cycle_size = 0
    j = i
    while not visited[j]:
        visited[j] = 1
        j = sorted_arr[j][1]
        cycle_size += 1
    ans += cycle_size - 1

print(ans)
