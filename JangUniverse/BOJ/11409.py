'''
ABCDE연속행렬 곱의 최솟값 =

min(ABCDE,

min(A) + min(BCDE) + 합치는 비용(A행 * A열 * E열),

min(AB) + min(CDE) + 합치는 비용(A행 * B열 * E열),

min(ABC) + min(DE) + 합치는 비용(A행 * C열 * E열),

min(ABCD) + min(E) + 합치는 비용(A행 * D열 * E열)

)
'''
import sys
input = sys.stdin.readline

n = int(input())
li = []
for _ in range(n):
    li.append(list(map(int, input().split())))

# DP 테이블: dp[i][j] = i번째부터 j번째 행렬까지의 최소 곱셈 연산 수
dp = [[0] * n for _ in range(n)]

for length in range(2, n + 1): 
    for i in range(n - length + 1):
        j = i + length - 1
        dp[i][j] = float('inf')
        
        for k in range(i, j):
            cost = dp[i][k] + dp[k+1][j] + li[i][0] * li[k][1] * li[j][1]
            dp[i][j] = min(dp[i][j], cost)

print(dp[0][n-1])