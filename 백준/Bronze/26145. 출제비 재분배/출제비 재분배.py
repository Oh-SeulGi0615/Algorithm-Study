n, m = map(int, input().split())

arr1 = list(map(int, input().split()))
arr2 = [0 for _ in range(m)]
arr1.extend(arr2)

money = arr1
for i in range(n):
    arr = list(map(int, input().split()))

    for j in range(len(arr)):
        if money[i] >= arr[j]:
            money[i] -= arr[j]
        else:
            money[i] = 0
        money[j] += arr[j]

print(*money)