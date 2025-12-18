import sys
input = sys.stdin.readline

n, c, w = map(int, input().split())
arr = [int(input()) for _ in range(n)]

best_price = 0
for cm in range(max(arr), 0, -1):
  price = 0
  for wood in arr:
    if wood == cm:
      price += wood * w
    elif wood > cm:
      if wood % cm == 0:
        price += max(0, (cm * w) * (wood // cm) - (c * ((wood // cm) - 1)))
      else:
        price += max(0, ((cm * w) - c) * (wood // cm))
  
  if price > best_price:
    best_price = price

print(best_price)