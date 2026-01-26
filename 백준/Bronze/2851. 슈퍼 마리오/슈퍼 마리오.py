import sys
input = sys.stdin.readline

arr = [0]
for _ in range(10):
  num = int(input())
  arr.append(arr[-1] + num)

if 100 in arr:
  print(100)
else:
  min_error = 10**9
  loc = 0
  for i in range(len(arr)):
    if abs(100 - arr[i]) < min_error:
      min_error = abs(100 - arr[i])
      loc = i
    elif abs(100 - arr[i]) == min_error and loc != i:
      loc = i
  print(arr[loc])