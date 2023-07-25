import sys
input = sys.stdin.readline

n, s, r = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

arr = [2 if i in list(map(lambda x: x-1, arr2)) else 1 for i in range(n)]

for i in range(len(arr)):
    if i in list(map(lambda x:x-1, arr1)):
        arr[i] -= 1

for i in range(len(arr)):
    if i == 0:
        if arr[i] == 0 and arr[i+1] == 2:
            arr[i] += 1
            arr[i+1] -= 1
    elif i == len(arr)-1:
        if arr[i] == 0 and arr[i-1] == 2:
            arr[i] += 1
            arr[i-1] -= 1
    else:
        if arr[i] == 0:
            if arr[i-1] == 2:
                arr[i] += 1
                arr[i-1] -= 1
            elif arr[i+1] == 2:
                arr[i] += 1
                arr[i+1] -= 1

print(arr.count(0))