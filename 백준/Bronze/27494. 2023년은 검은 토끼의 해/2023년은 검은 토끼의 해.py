n = int(input())

if n < 2023:
  print(0)
else:
  cnt = 0
  for i in range(2023, n+1):
    string = list(str(i))

    if '2' in string:
      string2 = string[string.index('2'):]
      if '0' in string2:
        string3 = string2[string2.index('0'):]
        if '2' in string3:
          string4 = string3[string3.index('2'):]
          if '3' in string4:
            cnt += 1
  print(cnt)