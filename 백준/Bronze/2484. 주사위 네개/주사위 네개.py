import sys
n = int(sys.stdin.readline())

best_score = 0
for _ in range(n):
  cnt = [0 for _ in range(7)]
  arr = list(map(int, sys.stdin.readline().split()))

  for i in arr:
    cnt[i] += 1

  if 4 in cnt:
    score = 50000 + (cnt.index(4) * 5000)
    if score > best_score:
      best_score = score
  
  elif 3 in cnt:
    score = 10000 + (cnt.index(3) * 1000)
    if score > best_score:
      best_score = score
  
  elif 2 in cnt:
    if cnt.count(2) == 2:
      score = 2000 + (cnt.index(2) * 500) + ((cnt[cnt.index(2)+1:].index(2) + cnt.index(2) + 1) * 500)
    elif cnt.count(2) == 1:
      score = 1000 + (cnt.index(2) * 100)
    
    if score > best_score:
      best_score = score
  
  else:
    score = max(arr) * 100
    if score > best_score:
      best_score = score
      
print(best_score)