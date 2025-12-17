import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
arr1 = [int(input()) for _ in range(n)]
arr2 = [int(input()) for _ in range(m)]

cost, item = 0, 0
f1, f2 = 0, 0
while True:
  if f1 >= len(arr1) or f2 >= len(arr2):
    break

  if arr1[f1] != 0:
    if arr2[f2] != 0:
      arr1[f1] -= 1
      arr2[f2] -= 1
      item += 1
      cost += (f1 + 1) + (f2 + 1)
    else:
      f2 += 1
  else:
    f1 += 1

print(item, cost)