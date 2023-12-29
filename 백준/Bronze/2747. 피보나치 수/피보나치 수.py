import sys
input = sys.stdin.readline

n = int(input())

arr = [0, 1]
idx = 2
while idx <= n:
    next = arr[idx - 2] + arr[idx - 1]
    arr.append(next)
    idx += 1

print(arr[-1])