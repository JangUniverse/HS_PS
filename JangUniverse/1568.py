def maxi(a, b, d):
    index = a
    ki = d[a]
    for i in range(a, b + 1):
        if d[i] > ki:
            index = i
            ki = d[i]
    return index
n = int(input())
d = [0] + list(map(int, input().split())) 
a, b = map(int, input().split())
print(maxi(a, b, d))
