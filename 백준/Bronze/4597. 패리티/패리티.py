while True:
  string = input()
  if string == '#':
    break
  
  string = list(string)
  cnt = 0
  for i in range(len(string)-1):
    if string[i] == '1':
      cnt += 1
  
  result = string[:-1]
  if string[-1] == 'e':
    if cnt % 2 == 0:
      result.append('0')
    else:
      result.append('1')
  else:
    if cnt % 2 == 0:
      result.append('1')
    else:
      result.append('0')
  
  print(''.join(result))