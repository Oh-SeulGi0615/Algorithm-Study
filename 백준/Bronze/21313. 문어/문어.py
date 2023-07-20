import sys
input = sys.stdin.readline

n = int(input())

arr = []
for i in range(n):
    if i < n-1:
        if len(arr) == 0:
            arr.append(1)
        elif arr[-1] == 1:
            arr.append(2)
        elif arr[-1] == 2:
            arr.append(1)
    else:
        if arr[i-1] == 2 and arr[0] == 1:
            arr.append(3)
        else:
            arr.append(2)

print(*arr)