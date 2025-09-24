a, b, c = map(int, input().split())
t = int(input())

if t <= 30:
  print(a)
else:
  fee = a
  extra = 0
  t_ = t - 30

  if t_ % b == 0:
    extra = t_ // b
  else:
    extra = t_ // b + 1
  
  fee += extra * c
  print(fee)