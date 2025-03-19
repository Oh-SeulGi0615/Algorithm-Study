n = int(input())

cnt = 0
for i in range(1, n//3 + 1):
  for j in range(i, max(n-i, i)):
    k = n-i-j
    if k < j:
      break
    if k < i+j:
      cnt += 1
print(cnt)