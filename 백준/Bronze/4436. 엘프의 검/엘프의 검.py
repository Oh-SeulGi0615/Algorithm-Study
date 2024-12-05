while True:
  try:
    n = int(input())
    check = [0 for _ in range(10)]

    k = 1
    while True:
      if 0 not in check:
        break

      arr = list(str(n * k))
      for num in arr:
        check[int(num)-1] += 1
      k += 1
    
    print(k-1)
  except:
    break