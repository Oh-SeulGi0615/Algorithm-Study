import sys
input = sys.stdin.readline

n = int(input())
arr = 'baby sukhwan tururu turu very cute tururu turu in bed tururu turu baby sukhwan'.split()

a, b = divmod(n, len(arr))

if (a == 0) or ('turu' not in arr[b-1]):
  print(arr[b-1])
elif (a > 0) and ('turu' in arr[b-1]):
  if (b-1) % 2 == 0:
    res = 'tururu' + ('ru' * a)
  else:
    res = 'turu' + ('ru' * a)

  if res.count('ru') < 5:
    print(res)
  else:
    print(f"tu+ru*{res.count('ru')}")