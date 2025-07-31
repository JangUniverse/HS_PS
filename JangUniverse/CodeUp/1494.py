k, n = map(int, input().split())
arr = [0] * (k+2) #arr 이 [1] to [k] --> k+2개의 length
arr2 = [0] * (k+2)

for _ in range(n):
    s, e, u = map(int, input().split())
    arr[s] += u
    arr[e + 1] -= u

for i in range(1, k + 1):
    print(arr[i], end=' ')
print()

for i in range(1, k + 1):
    arr2[i] = arr2[i - 1] + arr[i]
    print(arr2[i], end=' ')