import sys
input = sys.stdin.readline

a, p = map(int, input().split())

arr = [a]
num = arr[-1]
while True:
  res_arr = []

  while True:
    a, mod = divmod(num, 10)
    res_arr.append(mod)
    num = a

    if num < 10:
      res_arr.append(num)
      break
  
  res = sum(list(map(lambda x: x**p, res_arr)))
  if res in arr:
    arr.append(res)
    break

  arr.append(res)
  num = arr[-1]

print(len(arr[:arr.index(arr[-1])]))