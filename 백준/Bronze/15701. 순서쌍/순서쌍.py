import math

n = int(input())

cnt = 0
for i in range(1, int(math.sqrt(n)+1)):
  if n % i == 0:
    if int(math.sqrt(n)) == math.sqrt(n) and i == math.sqrt(n):
      cnt += 1
    else:
      cnt += 2

print(cnt)