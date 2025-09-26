n = int(input())
result = []
for _ in range(n):
  arr = input().split()
  name = arr[0]
  score, risk, cost = map(int, arr[1:])

  score_ = (score ** 3) / (cost * (risk + 1))
  result.append([int(score_), cost, name])

result = sorted(result, key=lambda x: (-x[0], x[1], x[2]))
print(result[1][-1])