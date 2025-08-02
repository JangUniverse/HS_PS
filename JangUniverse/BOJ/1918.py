import sys
input = sys.stdin.readline

n = input().strip()
ans = ''
stack = []

for i in n:
    if i.isalpha():
        ans += i
    else:
        if i == '(':
            stack.append(i)
        
        elif i == '*' or i == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                ans += stack.pop()
            stack.append(i)
        
        elif i == '+' or i == '-':
            while stack and stack[-1] != '(':  
                ans += stack.pop()
            stack.append(i)
        
        elif i == ')':
            while stack and stack[-1] != '(':
                ans += stack.pop()
            if stack:  # '(' 제거
                stack.pop()

while stack:
    ans += stack.pop()

print(ans)
