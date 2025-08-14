import sys
input = sys.stdin.readline
l = input().strip().split("|")
a_minor = ['A', 'D', 'E']
c_major = ['C', 'F', 'G']
acount = 0
ccount = 0

for i in l:
    if i[0] in a_minor:
        acount += 1
    if i[0] in c_major:
        ccount += 1
    
if acount == ccount:
    if l[-1][-1] in c_major:
        ccount += 1
    if l[-1][-1] in a_minor:
        acount += 1

if acount < ccount :
    print("C-major")
else:
    print("A-minor")