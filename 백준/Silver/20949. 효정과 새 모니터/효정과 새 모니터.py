import math

result = []
for i in range(int(input())):
  w, h = map(int, input().split())
  ppi = math.sqrt(w**2 + h**2) / 77

  result.append([i+1, ppi])

result = sorted(result, key=lambda x: (-x[1], x[0]))

for num in result:
  print(num[0])