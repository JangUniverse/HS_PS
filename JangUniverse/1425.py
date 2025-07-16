n, c = map(int, input().split())
li = list(map(int, input().split()))
li.sort()
for i in range(len(li)):
    if i%c == 0 and i != 0:
        print()
    print(li[i], end = ' ')