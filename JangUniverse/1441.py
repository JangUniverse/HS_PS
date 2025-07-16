li = list()
n = int(input())
for i in range(n):
    x = int(input())
    li.append(x)
for i in range(n-1):
    swapped = False
    for j in range(n-1):
        if li[j+1]<li[j]:
            li[j+1], li[j] = li[j], li[j+1]
            swapped = True
    if not swapped:
        break
        
for i in range(n):
    print(li[i])