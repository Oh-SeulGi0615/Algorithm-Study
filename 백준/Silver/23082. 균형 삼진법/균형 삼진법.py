def solution(num):
  result = ''
  while num > 0:
    num, mod = divmod(num, 3)
    result += str(mod)
  return list(result)

n = int(input())

a = solution(abs(n))
for i in range(len(a)):
  if a[i] == '2':
    a[i] = 'T'

    if i+1 >= len(a):
      a.append('0')
    a[i+1] = str(int(a[i+1]) + 1)
  elif a[i] == '3':
    a[i] = '0'
    if i+1 >= len(a):
      a.append('1')
    else:
      a[i+1] = str(int(a[i+1]) + 1)

if n > 0:
  print(''.join(a[::-1]))
elif n < 0:
  for i in range(len(a)):
    if a[i] == 'T':
      a[i] = '1'
    elif a[i] == '1':
      a[i] = 'T'
  print(''.join(a[::-1]))
else:
  print('0')