import math

n = int(input())
for _ in range(n):
  num = int(input())
  
  if math.sqrt(num) == math.ceil(math.sqrt(num)):
    print(1)
  else:
    print(0)