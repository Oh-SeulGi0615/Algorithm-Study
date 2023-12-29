import sys
input = sys.stdin.readline

arr = list(input().rstrip())

height = 10
for i in range(1, len(arr)):
    if arr[i] == arr[i-1]:
        height += 5
    else:
        height += 10

print(height)