import sys
input = sys.stdin.readline

arr = list(map(int, input().split()))
arr.sort()

d1 = arr[1] - arr[0]
d2 = arr[2] - arr[1]

if d1 == d2:
    print(arr[2] + d2)
elif d1 > d2:
    print(arr[1] - d2)
elif d1 < d2:
    print(arr[1] + d1)