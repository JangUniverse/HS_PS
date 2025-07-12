text = input()
res = ''

for c in text:
    if c.isalpha():     
        res += chr((ord(c) - ord('a') - 3) % 26 + ord('a'))
    else:
        res += c
print(res)
