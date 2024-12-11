arr = list(input())
result, stack, reverse = [], [], []
is_reverse = True

for i in arr:
  if i == '<':
    if is_reverse == True:
      is_reverse = False
    if reverse:
      string = ''.join(map(str, reverse))
      string = ' '.join(list(map(lambda x: x[::-1], string.split())))
      result.append(string)
      reverse = []
  elif i == '>':
    string = '<'+''.join(stack)+'>'
    result.append(string)
    is_reverse = True
    stack = []
  
  else:
    if is_reverse == True:
      reverse.append(i)
    else:
      stack.append(i)

if reverse:
  string = ''.join(map(str, reverse))
  string = ' '.join(list(map(lambda x: x[::-1], string.split())))
  result.append(string)
  reverse = []

print(''.join(result))