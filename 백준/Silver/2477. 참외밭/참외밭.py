import sys

k = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(6)] * 2

max_ew, max_ns = 0, 0
small_ew, small_ns = 0, 0

for i in range(2, len(arr)):
  if arr[i][0] in [1, 2] and arr[i][1] > max_ew:
    max_ew = arr[i][1]
  elif arr[i][0] in [3, 4] and arr[i][1] > max_ns:
    max_ns = arr[i][1]

  if arr[i-2][0] == 1 and arr[i-1][0] == 4 and arr[i][0] == 1:
    small_ew = arr[i][1]
    small_ns = arr[i-1][1]
  elif arr[i-2][0] == 4 and arr[i-1][0] == 2 and arr[i][0] == 4:
    small_ew = arr[i-1][1]
    small_ns = arr[i][1]
  elif arr[i-2][0] == 3 and arr[i-1][0] == 2 and arr[i][0] == 3:
    small_ew = arr[i-1][1]
    small_ns = arr[i-2][1]
  elif arr[i-2][0] == 3 and arr[i-1][0] == 1 and arr[i][0] == 3:
    small_ew = arr[i-1][1]
    small_ns = arr[i][1]

print(k * ((max_ew * max_ns) - (small_ew * small_ns)))