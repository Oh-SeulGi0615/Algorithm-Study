import sys
import math

c, k = map(int, sys.stdin.readline().split())

money = 10 ** k

if c % money != 0:
  if int(str(c / money).split('.')[1][0]) < 5:
    c = math.floor(c / money) * money
  else:
    c = math.ceil(c / money) * money

print(int(c))