import sys
input = sys.stdin.readline

t = input().rstrip()
p = input().rstrip()
res = 0
idx = []

def get_lps(pattern):
    m = len(pattern)
    lps = [0] * m
    length = 0
    i = 1
    
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp(text, pattern):
    global res, idx
    n, m = len(text), len(pattern)
    lps = get_lps(pattern)
    
    i, j = 0, 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
        
        if j == m:
            idx.append(i - j + 1)
            res += 1
            j = lps[j - 1]

kmp(t, p)
print(res)
print(*idx)