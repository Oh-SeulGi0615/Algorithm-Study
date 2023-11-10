import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

sum_ = arr[0]
for i in range(1, len(arr)):
    if arr[i] == arr[i-1] + 1:
        pass
    else:
        sum_ += arr[i]

print(sum_)