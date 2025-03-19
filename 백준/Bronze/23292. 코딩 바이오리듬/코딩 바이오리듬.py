from datetime import datetime

birth_day = input()
b_list = [birth_day[:4], birth_day[4:6], birth_day[-2:]]

best_score = 0
fastest_day = birth_day
for _ in range(int(input())):
  d = input()
  d_list = [d[:4], d[4:6], d[-2:]]

  result = 1
  for i in range(len(b_list)):
    sub = 0
    for j in range(len(b_list[i])):
      sub += (int(b_list[i][j]) - int(d_list[i][j])) ** 2
    
    result *= sub
  
  if result > best_score:
    best_score = result
    fastest_day = d
  elif result == best_score:
    if datetime(int(fastest_day[:4]), int(fastest_day[4:6]), int(fastest_day[-2:])) > datetime(int(b_list[0]), int(b_list[1]), int(b_list[2])):
      fastest_day = d

print(fastest_day)