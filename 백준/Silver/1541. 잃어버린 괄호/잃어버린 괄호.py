import sys
input = sys.stdin.readline

arr = list(input().split('-'))

for i in range(len(arr)):
    if '+' in arr[i]:
        arr[i] = sum(list(map(int, arr[i].split('+'))))
    else:
        arr[i] = int(arr[i])

if len(arr) > 1:
    sum_ = arr[0]
    for j in range(1, len(arr)):
        sum_ -= arr[j]
    print(sum_)
else:
    print(arr[0])