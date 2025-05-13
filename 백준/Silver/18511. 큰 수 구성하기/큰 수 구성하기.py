from itertools import product

n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

n_length = len(str(n))
comb = []
for i in range(1, n_length + 1):
  comb += list(product(arr, repeat=i))

result = 0
for i in comb:
  num = int(''.join(map(str, i)))
  if num <= n and num > result:
    result = num

print(result)