import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr.sort()

sum_ = sum(arr)
if sum_ % 2 != 0:
    for i in range(n):
        if arr[i] % 2 == 0:
            pass
        else:
            sum_ -= arr[i]
            if sum_ % 2 == 0:
                break
    print(sum_)
else:
    print(sum_)