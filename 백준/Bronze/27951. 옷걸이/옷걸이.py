import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
u, d = map(int, input().split())

arr_u = 0
arr_d = 0
arr_any = 0

for i in range(len(arr)):
  if arr[i] == 1:
    arr_u += 1
  elif arr[i] == 2:
    arr_d += 1
  else:
    arr_any += 1

status = 'NO'
if max((u - arr_u), 0) + max((d - arr_d), 0) == arr_any:
  status = 'YES'

print(status)
if status == 'YES':
  res = []
  for i in range(len(arr)):
    if arr[i] == 1:
      res.append('U')
      arr_u -= 1
      u -= 1
    elif arr[i] == 2:
      res.append('D')
      arr_d -= 1
      d -= 1
    else:
      res.append('3')
  
  for j in range(len(res)):
    if res[j] == '3':
      if u > 0:
        res[j] = 'U'
        u -= 1
      elif d > 0:
        res[j] = 'D'
        d -= 1
        
  print(''.join(res))