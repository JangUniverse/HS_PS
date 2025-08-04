import sys
input =sys.stdin.readline

s1 = [0] + list(input())
s2 = [0] + list(input())
len1 = len(s1)
len2 = len(s2)
li = [list([''] *len1) for _ in range(len2)]

for i in range(1, len2):
    for j in range(1, len1):
        if s1[j] == s2[i]:
            li[i][j] = li[i-1][j-1] + s1[j]
        else:
            if len(li[i][j-1]) > len(li[i-1][j]):
                li[i][j] = li[i][j-1]
            else:
                li[i][j] = li[i-1][j]

ans = len(li[-1][-1])-1#개행문자 제거
print(ans)
if ans != 0:
    print(li[-1][-1])