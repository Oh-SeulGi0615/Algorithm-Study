string = list(input())
table = {}
for i in range(65, 123):
  if 90 >= i >= 65:
    table[chr(i)] = i - 38
  elif 122 >= i >= 97:
    table[chr(i)] = i - 96

def check(num):
  for i in range(2, num):
    if num % i == 0:
      return False
  return True

total = 0
for char in string:
  total += table[char]

if total == 1:
  print('It is a prime word.')
else:
  if check(total) == True:
    print('It is a prime word.')
  else:
    print('It is not a prime word.')