n, m = map(int, input().split())
result = []
result_set = set()

rev_streak = 0
best_rev_streak = 0

for _ in range(n):
  arr = input().split()
  rev_streak = 0
  best_rev_streak = 0
  
  for i in range(m):
    if arr[i] == '.':
      rev_streak += 1
    elif arr[i] == '*':
      if rev_streak > best_rev_streak:
        best_rev_streak = rev_streak
        rev_streak = 0
      else:
        rev_streak = 0
  if rev_streak > best_rev_streak:
    best_rev_streak = rev_streak
    rev_streak = 0
  
  result.append([best_rev_streak, arr[-1]])
  result_set.add(best_rev_streak)

print(len(result_set))
for c in result:
  print(*c)