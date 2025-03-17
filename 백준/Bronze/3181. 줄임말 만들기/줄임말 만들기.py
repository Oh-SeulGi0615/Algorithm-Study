useless = ['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']

string = input().split()
result = ''
for i in range(len(string)):
  if i == 0:
    result += string[i][0].upper()
  elif i != 0 and string[i] not in useless:
    result += string[i][0].upper()

print(result)