import sys
input = sys.stdin.readline
import heapq

n = int(input())
left = []   
right = [] 

for i in range(n):
    num = int(input())
    
    # 첫 번째 수
    if i == 0:
        heapq.heappush(left, -num)
        print(num)
        continue
    
    mid = -left[0]
    
    if num <= mid:
        heapq.heappush(left, -num)
    else:
        heapq.heappush(right, num)
    
    if len(left) > len(right) + 1:
        val = -heapq.heappop(left)
        heapq.heappush(right, val)
    elif len(right) > len(left):
        val = heapq.heappop(right)
        heapq.heappush(left, -val)
    
    print(-left[0])