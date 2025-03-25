arr = list(map(int, input().split(':')))

h = 0
ms = 0
error = 0
for time in arr:
  if 0 > time or time >= 60:
    error += 1
  if 0 < time < 13:
    h += 1
  if 0 <= time <= 59:
    ms += 1

if h == 0 or error > 0:
  print(0)
else:
  print(h *(ms - 1))