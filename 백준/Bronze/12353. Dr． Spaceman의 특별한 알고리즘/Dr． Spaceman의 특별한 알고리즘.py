import sys
input = sys.stdin.readline

t = int(input())
for i in range(1, t+1):
  cases = input().rstrip().split()

  s = cases[0]
  f = list(map(int, cases[1].replace('"','').split('\'')))
  m = list(map(int, cases[2].replace('"','').split('\'')))

  if s == 'B':
    result = (f[0] * 12 + f[1]) + (m[0] * 12 + m[1]) + 5
  else:
    result = (f[0] * 12 + f[1]) + (m[0] * 12 + m[1]) - 5

  low_f, low_i = divmod((result - 8 + 1) // 2, 12)
  high_f, high_i = divmod((result + 8) // 2, 12)
  
  print(f'Case #{i}: {int(low_f)}\'{int(low_i)}" to {int(high_f)}\'{int(high_i)}"')