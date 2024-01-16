import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

if arr[2] - arr[1] == arr[1] - arr[0]:
    q = arr[1] - arr[0]
    result = arr[0] + (q * n)
    print(result)

else:
    q = int(arr[1] / arr[0])
    result = arr[0] * (q ** n)
    print(result)