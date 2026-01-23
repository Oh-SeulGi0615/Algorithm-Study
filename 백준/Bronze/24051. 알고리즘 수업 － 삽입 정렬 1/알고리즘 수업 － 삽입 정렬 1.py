import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

change_num = []
for i in range(1, n):
  loc = i - 1
  item = arr[i]

  while 0 <= loc and item < arr[loc]:
    arr[loc + 1] = arr[loc]
    loc -= 1
    change_num.append(arr[loc + 1])
  
  if (loc + 1 != i):
    arr[loc + 1] = item
    change_num.append(arr[loc + 1])

if len(change_num) <= k:
  print(-1)
else:
  print(change_num[k-1])