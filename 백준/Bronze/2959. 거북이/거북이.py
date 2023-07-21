import sys
input = sys.stdin.readline

arr = list(map(int, input().split()))
arr.sort()

result = arr[0] * arr[2]
print(result)