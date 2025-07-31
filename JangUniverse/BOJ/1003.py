import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    x= int(input())
    a, b = 1, 0
    for i in range(x):
        a, b = b, a+b
    print(a,b)
#n일 때의 0 호출 횟수 = n-1일 때의 1 호출 횟수
#n일 때의 1 호출 횟수 = n-1일 때의 0 + 1 호출 횟수
