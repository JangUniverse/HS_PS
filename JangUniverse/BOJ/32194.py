import sys
input = sys.stdin.readline

n = int(input())
answers = [1]
prefix_sum = [0, 1]

for i in range(n):
    type_q, x, y = map(int, input().split())
    
    range_sum = prefix_sum[y] - prefix_sum[x-1]
    range_length = y - x + 1
    
    if type_q == 1:  # x~y가 모두 "예"인가?
        result = (range_sum == range_length)
    else:  # x~y가 모두 "아니오"인가?
        result = (range_sum == 0)
    answers.append(1 if result else 0)
    prefix_sum.append(prefix_sum[-1] + (1 if result else 0))
    
    print("Yes" if result else "No")