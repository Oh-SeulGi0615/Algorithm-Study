while True:
  try:
    n, k = map(int, input().split())

    chicken = n
    c = n
    while True:
      if c < k:
        break
      chicken += c // k
      c = (c % k) + (c // k)
      
    print(chicken)
  except:
    break