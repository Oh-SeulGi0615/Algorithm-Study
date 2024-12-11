arr = list(input().replace('()', 'l'))

cnt = 0
stack = []

for i in arr:
  if i == '(':
    stack.append('(')
  elif i == ')':
    stack.pop()
    cnt += 1
  elif i == 'l':
    cnt += stack.count('(')

print(cnt)