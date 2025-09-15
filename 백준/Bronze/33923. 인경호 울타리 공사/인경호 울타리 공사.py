n, m = map(int, input().split())

if n != m:
  result = (min(n, m) - 1) ** 2
  print(result)
else:
  result = ((n - 2) * 2) + (n - 3) ** 2
  print(result)