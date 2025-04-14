while True:
  s = int(input())
  if s == 0:
    break

  arr = []
  arr.append(s)
  while True:
    if s < 10:
      break
    
    result = 1
    arr2 = list(map(int, list(str(s))))
    for i in arr2:
      result *= i
    
    arr.append(result)
    s = result
  
  print(*arr)