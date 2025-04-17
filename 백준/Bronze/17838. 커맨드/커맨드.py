t = int(input())
for _ in range(t):
  string = list(input())

  if len(string) != 7:
    print(0)
  elif len(list(set(string))) != 2:
    print(0)
  elif string[0] == string[1] == string[4] and string[2] == string[3] == string[5] == string[6] and string[0] != string[2]:
    print(1)
  else:
    print(0)