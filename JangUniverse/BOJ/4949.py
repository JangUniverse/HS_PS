import sys
input = sys.stdin.readline

while 1:
    s = input().rstrip()
    if s == '.':
        break
    
    stack = []
    flag = True

    for i in range(len(s)):
        if s[i] == '(' or s[i] == '[':
            stack.append(s[i])
        elif stack and (s[i] == ')' or s[i] == ']'):
            if s[i] == ')' and stack[-1] == '(':
                stack.pop()
            elif s[i] == ']' and stack[-1] == '[': 
                stack.pop()
            else:
                flag = False
                break 
        elif not stack and (s[i] == ')' or s[i] == ']'):
            flag = False
            break 
        
    if flag and not stack:
        print('yes')
    else:
        print('no')