dict_ = {}
for i in range(1, 100001):
  best_score = i
  n = i

  while True:
    if n == 1:
      break

    if n % 2 == 0:
      n = int(n/2)
      if n > best_score:
        best_score = n
    else:
      n = (3*n)+1
      if n > best_score:
        best_score = n

  dict_[i] = best_score

for _ in range(int(input())):
  a = int(input())
  print(dict_[a])