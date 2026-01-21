import sys
input = sys.stdin.readline

n, m = map(int, input().split())
string = list(input().rstrip())[::-1]

res = ''
for i in range(len(string)):
  if len(res) == 0:
    if string[i] in ['A', 'E', 'I', 'O', 'U']:
      continue
    else:
      res += string[i]
  
  elif len(res) == 1 or len(res) == 2:
    if string[i] == 'A':
      res += string[i]
  
  elif len(res) < m:
    res += string[i]

if (len(res) < m) or ('AA' not in res):
  print('NO')
else:
  print('YES')
  print(res[::-1])