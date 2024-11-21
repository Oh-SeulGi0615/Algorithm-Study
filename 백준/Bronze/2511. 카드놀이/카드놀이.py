arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))

score_a, score_b, last_winner = 0, 0, ''
for i in range(len(arr_a)):
  if arr_a[i] > arr_b[i]:
    score_a += 3
    last_winner = 'A'
  elif arr_b[i] > arr_a[i]:
    score_b += 3
    last_winner = 'B'
  elif arr_a[i] == arr_b[i]:
    score_a += 1
    score_b += 1

if score_a > score_b:
  print(score_a, score_b)
  print('A')
elif score_b > score_a:
  print(score_a, score_b)
  print('B')
elif score_a == score_b:
  if last_winner:
    print(score_a, score_b)
    print(last_winner)
  else:
    print(score_a, score_b)
    print('D')