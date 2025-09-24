arr = list(map(int, list(input())))

state = -1
dict_ = {2:0, 0:0, 1:0, 8:0}

for num in arr:
  if num not in dict_.keys():
    state = 0
  else:
    dict_[num] += 1

if state != 0:
  values = dict_.values()

  if 0 in values:
    state = 1
  elif len(set(values)) > 1:
    state = 2
  else:
    state = 8

print(state)