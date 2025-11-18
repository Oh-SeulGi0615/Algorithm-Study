import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  string = list(input().rstrip().replace(' ',''))

  char_set = {chr(i):0 for i in range(97, 123)}
  for char in string:
    char_set[char] += 1

  values = list(char_set.values())
  max_val = max(values)
  if values.count(max_val) > 1:
    print('?')
  else:
    idx = values.index(max_val)
    print(chr(97 + idx))