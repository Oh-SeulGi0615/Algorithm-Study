n, m = map(int, input().split())

answer = ''
if len(str(n))*n <= m:
  answer = str(n) * n
else:
  while m > 0:
    if m >= len(str(n)):
      answer += str(n)
      m -= len(str(n))
    else:
      answer += str(n)[:m]
      m = 0

print(answer)