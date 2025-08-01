import sys
from bisect import bisect_left
input = sys.stdin.readline

def lis(li):
    dp = []
    for num in li:
        pos = bisect_left(dp, num)
        if pos == len(dp):
            dp.append(num)
        else:
            dp[pos] = num
    return dp

n = int(input())
li = list(map(int, input().split()))
res = len(lis(li))
print(res)