import sys
input = sys.stdin.readline

f = ' '+input().strip()
s = ' '+input().strip()

len_f = len(f)
len_s = len(s)

dp = list([0]*len_f for _ in range(len_s))
#if 좌대각 값 same --> +1 좌대각
#else: 그냥 좌대각 값 갖다쓰기
for i in range(1, len_s):
    for j in range(1, len_f):
        if f[j] == s[i]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])
print(dp[len_s-1][len_f-1])
