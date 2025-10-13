n = int(input())

score = {i:0 for i in range(n)}
game1, game2, game3 = [], [], []
for _ in range(n):
  arr = list(map(int, input().split()))

  game1.append(arr[0])
  game2.append(arr[1])
  game3.append(arr[2])

for i in range(n):
  if game1.count(game1[i]) == 1:
    score[i] += game1[i]
  if game2.count(game2[i]) == 1:
    score[i] += game2[i]
  if game3.count(game3[i]) == 1:
    score[i] += game3[i]

print(*score.values(), sep='\n')