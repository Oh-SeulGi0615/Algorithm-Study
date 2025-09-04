string = input().split('(')

if len(string) == 1:
  print(string[0])
  print('-')
else:
  print(string[0].rstrip())
  print(string[1][:-1].rstrip())