string = list(input())

cnt = 1
for i in range(len(string)):
  if i == 0:
    if string[i] == 'c':
      cnt *= 26
    else:
      cnt *= 10
  
  else:
    if string[i] == 'c' and string[i-1] == 'c':
      cnt *= 25
    elif string[i] == 'd' and string[i-1] == 'd':
      cnt *= 9
    elif string[i] == 'c' and string[i-1] == 'd':
      cnt *= 26
    elif string[i] == 'd' and string[i-1] == 'c':
      cnt *= 10

print(cnt)