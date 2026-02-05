import sys
input = sys.stdin.readline

n = int(input())
arr = [0, 0, 0, 10**9, 10**9, 10**9]

for _ in range(n):
  loc = list(map(int, input().split()))

  for i in range(6):
    if i < 3 and loc[i] > arr[i]:
      arr[i] = loc[i]
    elif i >=3 and loc[i] < arr[i]:
      arr[i] = loc[i]

if (arr[3] - arr[0] < 0) or (arr[4] - arr[1] < 0) or (arr[5] - arr[2] < 0):
  print(0)
else:
  res = (arr[3] - arr[0]) * (arr[4] - arr[1]) * (arr[5] - arr[2])
  print(res)