import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
for _ in range(m):
  a, b, c = map(int, input().split())

  if a == 1:
    arr[b-1] = c
  elif a == 2:
    for i in range(b-1, c):
      if arr[i] == 0:
        arr[i] = 1
      else:
        arr[i] = 0
  elif a == 3:
    arr[b-1:c] = [0] * (c - b + 1)
  else:
    arr[b-1:c] = [1] * (c - b + 1)
  
print(*arr)