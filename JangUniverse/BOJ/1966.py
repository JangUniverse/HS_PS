import sys
from collections import deque 
input = sys.stdin.readline

T = int(input())

for _ in range(T):
	
	n, m = map(int, input().split())
	priority = list(map(int, input().split()))
	q = deque([(priority[i], i) for i in range(n)])
	cnt = 0
	while q:
		
		flag = False
		for i in range(len(q)):
			
			if q[0][0] < q[i][0]:
				q.append(q.popleft())
				flag = True
				break
		if not flag:
			res = q.popleft()
			cnt += 1
			if res[1] == m:
				print(cnt)
				break