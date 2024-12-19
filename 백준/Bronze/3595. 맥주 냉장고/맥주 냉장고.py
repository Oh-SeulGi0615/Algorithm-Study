import math
n = int(input())

result = math.inf
answer = []

for i in range(1, n+1):
  for j in range(1, (int(n/i) + 1)):
    k = int((n / i) / j)

    if i * j * k == n:
      surface = (2 * (i * j)) + (2 * (k * j)) + (2 * (i * k))
      if surface < result:
        result = surface
        answer = [i, j, k]
        
print(*answer)