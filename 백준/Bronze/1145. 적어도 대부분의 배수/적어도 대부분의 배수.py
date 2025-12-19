import sys
input = sys.stdin.readline

arr = list(map(int, input().split()))
arr = sorted(arr)

for i in range(arr[0], arr[0]*arr[1]*arr[2] + 1):
  res = list(map(lambda x: True if i % x == 0 else False, arr))
  if res.count(True) >= 3:
    print(i)
    break