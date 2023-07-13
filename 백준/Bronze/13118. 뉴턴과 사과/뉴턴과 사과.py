import sys
input = sys.stdin.readline

arr = list(map(int, input().split()))
x, y, r = map(int, input().split())

for i in range(len(arr)):
    if x not in arr:
        print(0)
        break
    if arr[i] == x:
        print(i+1)