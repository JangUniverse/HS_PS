import sys
input = sys.stdin.readline
res = 0
#등차수열로 만들기 위한 최소 횟수
def even_dif(x, y, z):
    return (z-x)//2 + (z-y)//2


x, y, z = map(int, input().split())
num = sorted([x,y,z])
x = num[0]
y = num[1]
z = num[2]

if (y-x) %2 != 0 and (z-y)%2 != 0: #둘 다 홀수차이 --> 2회는 조정
    res = 2 + even_dif(x+1, y+2, z+1)

elif (y-x) %2 == 0 and (z-y) % 2 != 0: #1회
    res = 1+even_dif(x+1, y+1, z)

elif (y-x) %2 != 0 and (z-y) % 2 == 0:
    res = 1+even_dif(x, y+1, z+1)
else:
    res = even_dif(x,y,z)
print(res)