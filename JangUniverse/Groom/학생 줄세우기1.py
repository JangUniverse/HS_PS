import sys
input = sys.stdin.readline
#LIS날먹
n = int(input())
arr = list(map(int, input().split()))

pos = [0] * (n + 1)
for i in range(n):
    pos[arr[i]] = i
    
max_len = 1
cur_len = 1
for i in range(1, n):
    if pos[i] < pos[i + 1]:
        cur_len += 1
        max_len = max(max_len, cur_len)
    else:
        cur_len = 1

print(n - max_len)
