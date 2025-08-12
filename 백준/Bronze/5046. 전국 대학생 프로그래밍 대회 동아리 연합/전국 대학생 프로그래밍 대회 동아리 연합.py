n, b, h, w = map(int, input().split())

min_price = 1e9
for _ in range(h):
  p = int(input())
  arr = list(map(int, input().split()))

  for i in arr:
    if i >= n and p * n <= min_price:
      min_price = p * n

if min_price <= b:
  print(min_price)
else:
  print('stay home')