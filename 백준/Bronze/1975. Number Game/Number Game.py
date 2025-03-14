def func(arr, n, x):
  a, b = divmod(n, x)
  arr.append(b)
  if a >= x:
    func(arr, a, x)
  else:
    arr.append(a)

t = int(input())
for _ in range(t):
  n = int(input())
  cnt = 0

  for i in range(2, n+1):
    arr = []
    func(arr, n, i)

    for i in range(len(arr)):
      if arr[i] == 0:
        cnt += 1
      else:
        break

  print(cnt)