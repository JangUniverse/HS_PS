import sys
input =sys.stdin.readline
#[x1, y1, x2, y2]
x1, y1, x2, y2 = list(map(int, input().split()))
x3, y3, x4, y4 = list(map(int, input().split()))
#ccw
def ccw(x1, y1, x2, y2, x3, y3): #1->2->3
    ccw = (x2-x1)*(y3-y1)-(x3-x1)*(y2-y1)
    if ccw:
        ccw //= abs(ccw) #단위벡터로 만들기
    return ccw
ccw3 = ccw(x1, y1, x2, y2, x3, y3)
ccw4 = ccw(x1, y1, x2, y2, x4, y4)
ccw1 = ccw(x3, y3, x4, y4, x1, y1)
ccw2 = ccw(x3, y3, x4, y4, x2, y2) 

if ccw1 * ccw2 == 1 or ccw3 * ccw4 == 1:
    print(0) #구분됨
elif ccw1 == 0 and ccw2 == 0: #일직선상이면
    if x1 == x2: #l1이 수직선
        if max(y1, y2) < min(y3, y4) or max(y3, y4) < min(y1, y2):
            print(0)
        else:   
            print(1)
    else:
        if max(x1, x2) < min(x3, x4) or max(x3, x4) < min(x1, x2):
            print(0)
        else:
            print(1)
else:
    print(1)