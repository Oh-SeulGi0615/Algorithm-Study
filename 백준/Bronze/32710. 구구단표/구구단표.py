n = int(input())

arr = []
for i in range(1, 10):
  for j in range(1, 10):
    arr.append(i * j)

if n in arr:
  print(1)
else:
  print(0)