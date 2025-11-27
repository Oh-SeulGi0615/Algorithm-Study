import sys
input = sys.stdin.readline

n = int(input())

arr = [True] * 50000
for i in range(2, len(arr)):
  if arr[i] == True:
    for j in range(i*i, len(arr), i):
      arr[j] = False
res = [idx for idx in range(2, len(arr)) if arr[idx] == True]

mul_prime = []
for k in range(len(res)):
  for l in range(k, len(res)):
    if k == l:
      continue
    elif res[k] * res[l] > 200000:
      break
    else:
      mul_prime.append(res[k] * res[l])

mul_prime = sorted(mul_prime)

for _ in range(n):
  k = int(input())

  for num in mul_prime:
    if num >= k:
      print(num)
      break