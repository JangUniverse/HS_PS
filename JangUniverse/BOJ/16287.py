import sys
input =sys.stdin.readline

w, n = map(int, input().split())
li = sorted(list(map(int, input().split())))
visited = [0]*(w+1)

for i in range(len(li)+1):
    for j in range(i+1, len(li)):
        v = li[i] + li[j]
        if v > w:
            break

        visited[v] = (i, j)
    
for i in range(len(li)+1):
    for j in range(i+1, len(li)):
        v = li[i] + li[j]
        if v > w:
            break
        
        if visited[w-v] and i not in visited[w-v] and j not in visited[w-v]:
            print("YES")
            exit()

print("NO")
