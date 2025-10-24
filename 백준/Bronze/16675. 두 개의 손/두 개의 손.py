import sys

ml, mr, tl, tr = sys.stdin.readline().split()

case_m, case_t = [], []
for cm in [ml, mr, tl, tr]:
  count = []

  if cm in [ml, mr]:
    arr = [tl, tr]
  else:
    arr = [ml, mr]

  for ct in arr:
    if cm == 'R':
      if ct == 'R':
        count.append(False)
      elif ct == 'S':
        count.append(True)
      else:
        count.append(False)
    
    if cm == 'S':
      if ct == 'S':
        count.append(False)
      elif ct == 'P':
        count.append(True)
      else:
        count.append(False)
    
    if cm == 'P':
      if ct == 'P':
        count.append(False)
      elif ct == 'R':
        count.append(True)
      else:
        count.append(False)

  if cm in [ml, mr]:
    case_m.append(count)
  else:
    case_t.append(count)

if [True, True] in case_m:
  print('MS')
elif [True, True] in case_t:
  print('TK')
else:
  print('?')