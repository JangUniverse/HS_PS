lotto = list(map(int, input().split()))
number = list(map(int, input().split()))
count = 0
special = 0
for i in range(6):
    for j in number:
        if j == lotto[i]:
            count += 1
        else:
            continue
for i in range(6):
    if number[i] == lotto[-1]:
        special += 1


if lotto[-1] == number[-1]:
    special = 1
if count == 6:
    print(1)
if count == 5 and special == 1:
    print(2)
if count == 5 and special == 0:
    print(3)
if count == 4:
    print(4)
if count == 3:
    print(5)
if count <= 2:
    print(0)