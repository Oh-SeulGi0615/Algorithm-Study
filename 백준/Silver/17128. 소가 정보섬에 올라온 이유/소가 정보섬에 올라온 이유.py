import sys

n, q = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))
arr.extend([arr[0], arr[1], arr[2]])

q_list = list(map(int, sys.stdin.readline().split()))
q_ = [-3, -2, -1, 0]

score = []
for i in range(len(arr)-3):
  score_ = arr[i] * arr[i+1] * arr[i+2] * arr[i+3]
  score.append(score_)
sum_score = sum(score)

for q in q_list:
  q_ = list(map(lambda x: x+(q-1), q_))
  for i in q_:
    score[i] *= -1
    sum_score += 2*score[i]
  print(sum_score)
  q_ = [-3, -2, -1, 0]