import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

sq_sum = 0
for num in arr:
  sq_sum += num ** 2

result = int((sum(arr)**2 - sq_sum) / 2)
print(result)