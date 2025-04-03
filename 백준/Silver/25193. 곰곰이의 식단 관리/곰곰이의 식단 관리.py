import math
n = int(input())
string = input()

not_chicken = len(string.replace('C', ''))
chicken = string.count('C')

if not_chicken == 0:
  print(n)
else:
  print(math.ceil(chicken / (not_chicken + 1)))