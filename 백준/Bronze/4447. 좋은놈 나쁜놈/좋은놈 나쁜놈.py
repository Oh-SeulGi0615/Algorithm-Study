n = int(input())
for _ in range(n):
  name = input()
  char = list(name.lower())
  g = char.count('g')
  b = char.count('b')

  if g > b:
    print(f'{name} is GOOD')
  elif g < b:
    print(f'{name} is A BADDY')
  else:
    print(f'{name} is NEUTRAL')