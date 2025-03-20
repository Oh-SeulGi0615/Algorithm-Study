n = int(input())

if n <= 4:
  print(4)
else:
  l, s, h, v = 2, 4, 1, 1

  while True:
    next_l = l + 1
    next_s = s + (2*next_l-1)
    if s <= n <= next_s:
      break
    
    l += 1
    s = next_s
    h += 1
    v += 1

  remain = n - s
  if remain > l:
    print((2*((h+1)+(v+1))))
  else:
    print((2*((h+1)+v)))