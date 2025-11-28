import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
  string = list(input().rstrip().lower().replace(' ', ''))
  chars = [0 for _ in range(26)]

  for char in string:
    if 97 <= ord(char) <= 122:
      chars[ord(char) - 97] += 1

  if 0 not in chars:
    print('pangram')
  else:
    res = ''
    for i in range(len(chars)):
      if chars[i] == 0:
        res += chr(i + 97)
    print(f'missing {res}')