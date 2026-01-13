import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  num = input().rstrip()
  arr = list(map(int, num))

  s, e = 0, 0
  for i in range(len(arr)-1, 0, -1):
    if arr[i] > arr[i-1]:
      if not s:
        s = i - 1
  
  for j in range(len(arr)-1, s, -1):
    if arr[j] > arr[s]:
      if not e:
        e = j

  if s == 0 and e == 0:
    print('BIGGEST')
  else:
    arr[s], arr[e] = arr[e], arr[s]
    arr[s+1:] = arr[s+1:][::-1]
    res = ''.join(list(map(str, arr)))
    print(int(res))