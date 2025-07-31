def quick(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr[1:] if x > pivot]

    return quick(left) + mid + quick(right)
n = int(input())
li = []
for i in range(n):
    li.append(int(input()))
res = quick(li)
for i in range(n):
    print(res[i])