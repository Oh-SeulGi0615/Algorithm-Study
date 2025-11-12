import sys

s = int(sys.stdin.readline())

if s % 4763 != 0:
  print(0)
else:
  s //= 4763

  result = []
  for i in range(200):
    s1 = s - (i * 508)
    s2 = s - (i * 108)

    if s1 % 212 == 0 and (0 <= s1 // 212 <= 200):
      result.append([i, s1 // 212])
    elif s1 % 305 == 0 and (0 <= s1 // 305 <= 200):
      result.append([i, s1 // 305])
    elif s2 % 212 == 0 and (0 <= s2 // 212 <= 200):
      result.append([i, s2 // 212])
    elif s2 % 305 == 0 and (0 <= s2 // 305 <= 200):
      result.append([i, s2 // 305])

  result = sorted(result, key=lambda x: (x[0], x[1]))

  print(len(result))
  for case in result:
    print(*case)