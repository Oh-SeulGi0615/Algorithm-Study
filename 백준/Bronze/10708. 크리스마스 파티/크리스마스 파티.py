n = int(input())
m = int(input())
target = list(map(int, input().split()))
score = {i:0 for i in range(1, n+1)}

for turn in range(m):
  choices = list(map(int, input().split()))

  for idx in range(n):
    if idx == target[turn]-1:
      score[choices[idx]] += 1
    elif choices[idx] == target[turn]:
      score[idx+1] += 1
    elif choices[idx] != target[turn]:
      score[target[turn]] += 1

print(*score.values(), sep='\n')