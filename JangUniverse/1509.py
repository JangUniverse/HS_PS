jido = [list(map(int, input().split())) for _ in range(10)] 
people = list(map(int,input().split()))
res = [0]*10
count = 0
for x in range(10):
    if people[x] != 0: #human?
        for y in range(9, -1, -1):
            if jido[y][x] > 0:
                print(x+1, 'crash')
                break
            elif jido[y][x] <0:
                print(x+1, 'fall')
                break
            else:
                count += 1
                continue
        if count == 10:
            print(x+1, 'safe')
        count = 0