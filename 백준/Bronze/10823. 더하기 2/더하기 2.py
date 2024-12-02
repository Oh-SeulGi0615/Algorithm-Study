s = ''
while True:
  try:
    string = input().rstrip()
    s += string
  except:
    break

print(sum(list(map(int, s.split(',')))))