n = int(input())
arr = list(input())

odd, even = 0, 0
for num in arr:
  if int(num) % 2 == 0:
    even += 1
  else:
    odd += 1

if even > odd:
  print(0)
elif even < odd:
  print(1)
else:
  print(-1)