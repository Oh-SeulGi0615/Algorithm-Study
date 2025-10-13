def convert(num, b):
  result = ''
  if num == 0:
    result = '0'
  else:
    while num > 0:
      num, mod = divmod(num, b)
      result += str(mod)

  return result[::-1]

while True:
  arr = list(map(int, input().split()))
  if arr[0] == 0:
    break
  
  if arr[0] != 10:
    p = int(str(arr[1]), arr[0])
    m = int(str(arr[2]), arr[0])
    mod = p % m
    print(convert(mod, arr[0]))
  else:
    p = arr[1]
    m = arr[2]
    mod = p % m
    print(mod)