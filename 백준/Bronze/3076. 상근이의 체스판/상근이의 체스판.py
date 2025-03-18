r, c = map(int, input().split())
a, b = map(int, input().split())

arr = []
black = True
for i in range(r*a):
  arr2 = []
  if (i // a) % 2 == 0:
    for j in range(c*b):
      if (j // b) % 2 == 0:
        arr2.append('X')
      else:
        arr2.append('.')
  else:
    for j in range(c*b):
      if (j // b) % 2 == 0:
        arr2.append('.')
      else:
        arr2.append('X')

  arr.append(arr2)

for l in arr:
  print(''.join(l))