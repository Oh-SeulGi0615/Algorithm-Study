import sys
input = sys.stdin.readline

n = int(input())

arr = [1, 1]
while n > 0:
    if arr[0] == arr[1]:
        arr[0] += 1
    else:
        arr[1] += 1
    n -= 1

print(arr[0] * arr[1])