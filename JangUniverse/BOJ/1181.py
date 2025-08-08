n = int(input())
li = list(input() for _ in range(n))
li = list(set(li))
li = sorted(li, key= lambda x: [len(x), x])
for word in li:
    print(word, end = '\n')