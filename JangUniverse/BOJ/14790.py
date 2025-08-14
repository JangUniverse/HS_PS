import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    num = int(input())
    for i in range(num, 0, -1):
        if str(i) == "".join(sorted(list(str(i)))): 
            print(f"Case #{_+1}: {i}")
            break