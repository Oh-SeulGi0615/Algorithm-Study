import sys
input = sys.stdin.readline

l, r = map(int, input().split())

if len(str(l)) != len(str(r)):
  print(0)

else:
  arr_l = list(map(int, list(str(l))))
  arr_r = list(map(int, list(str(r))))

  cnt = 0
  for i in range(len(arr_r)):
    if arr_l[i] == arr_r[i] == 8:
      cnt += 1
    elif arr_l[i] == arr_r[i]:
      continue
    else:
      break

  print(cnt)