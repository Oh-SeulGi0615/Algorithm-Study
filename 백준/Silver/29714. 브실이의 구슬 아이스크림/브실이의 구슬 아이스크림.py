import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr_dict = {}
for i in arr:
  if i not in arr_dict:
    arr_dict[i] = 1
  else:
    arr_dict[i] += 1

q = int(input())
for _ in range(q):
  arr1 = list(map(int, input().split()))[1:]
  arr2 = list(map(int, input().split()))[1:]

  arr1_dict = {}
  for j in arr1:
    if j not in arr1_dict:
      arr1_dict[j] = 1
    else:
      arr1_dict[j] += 1

  res = all(arr1_dict[k] <= arr_dict.get(k, 0) for k in arr1_dict)
  if res:
    arr2_dict = {}
    for k in arr2:
      if k not in arr2_dict:
        arr2_dict[k] = 1
      else:
        arr2_dict[k] += 1

    for k, v in arr1_dict.items():
      arr_dict[k] -= v

    for k, v in arr2_dict.items():
      if k not in arr_dict:
        arr_dict[k] = v
      else:
        arr_dict[k] += v

result = []
cnt = 0
for k, v in arr_dict.items():
  result += [k] * v
  cnt += v

if cnt == 0:
  print(0)
else:
  print(cnt)
  print(*result)