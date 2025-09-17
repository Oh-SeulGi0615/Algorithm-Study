lkp = {'l':0, 'k':0, 'p':0}
for _ in range(3):
  string = input().rstrip()
  if string[0] in lkp:
    lkp[string[0]] += 1

if 0 in lkp.values():
  print('PONIX')
else:
  print('GLOBAL')