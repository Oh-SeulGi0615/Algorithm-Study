old = list(input())
new = []

for char in old:
  if ord(char) < 97:
    if len(new) % 4 != 0:
      for i in range(4-(len(new)%4)):
        new.append('NOP')
    new.append(char)
  else:
    new.append(char)

print(new.count('NOP'))