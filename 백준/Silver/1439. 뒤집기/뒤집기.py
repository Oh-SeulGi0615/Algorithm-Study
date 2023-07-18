import sys
input = sys.stdin.readline

arr = list(input().rstrip())

arr2 = []
for i in range(len(arr)):
    if i == 0:
        arr2.append(int(arr[i]))
    if arr[i] != arr[i-1]:
        arr2.append(int(arr[i]))

print(min(arr2.count(0), arr2.count(1)))