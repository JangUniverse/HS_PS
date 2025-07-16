n=int(input())
list=[]
for i in range(0, n):
    a,b=map(int,input().split())
    list.append([i+1,a,b])
result = sorted(list, key=lambda x:(x[1],x[2],-x[0]), reverse=True)
for i in result:
    print(i[0],i[1],i[2])