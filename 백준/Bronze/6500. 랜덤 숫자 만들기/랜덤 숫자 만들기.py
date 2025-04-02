while True:
  n = input()
  if n == '0':
    break
  
  cnt = 1
  arr = [n]

  while True:
    n_ = str(int(n) ** 2).zfill(8)[2:6]
    if n_ in arr:
      break

    n = n_
    arr.append(n)
    cnt += 1

  print(cnt)