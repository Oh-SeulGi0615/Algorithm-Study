import sys

n = int(sys.stdin.readline())

result1 = 0
result2 = 0

for i in range(1, n+1):
  result1 += i
  result2 += i**3

print(result1, result1**2, result2, sep='\n')