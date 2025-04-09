import sys

t = int(sys.stdin.readline())
for _ in range(t):
  k = int(sys.stdin.readline())
  students = list(map(int, sys.stdin.readline().split()))

  pass_students = 0
  best_score = 23*60 + 59
  best_student = 0

  n = int(sys.stdin.readline())
  for _ in range(n):
    score = list(map(int, sys.stdin.readline().split()))
    player = score[0]
    
    if score[1] == -1:
      lab_time = -1
    else:
      lab_time = score[1] * 60 + score[2]

    if player in students and lab_time != -1 and lab_time <= 360:
      pass_students += 1
      if lab_time < best_score:
        best_score = lab_time
        best_student = player
  
  print(best_student, pass_students)