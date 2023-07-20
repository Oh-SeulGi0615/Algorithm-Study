import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr2 = [0 for i in range(n)]
sum_ = 0
for i in range(len(arr)):
    if arr[i] == 0:
        sum_ = 0
        arr[i] = sum_
    else:
        if arr[i-1] == 0:
            sum_ += 1
            arr2[i] = sum_
        else:
            sum_ += 1
            arr2[i] = sum_

print(sum(arr2))