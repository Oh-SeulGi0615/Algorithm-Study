n = int(input())
dp_table = []
costs = []
for _ in range(n):
  r, g, b = map(int, input().split())
  cost = [r, g, b]
  costs.append(cost)

dp_table.append(costs[0])

for i in range(1, n):
  r = costs[i][0] + min(dp_table[i-1][1], dp_table[i-1][2])
  g = costs[i][1] + min(dp_table[i-1][2], dp_table[i-1][0])
  b = costs[i][2] + min(dp_table[i-1][0], dp_table[i-1][1])
  dp_table.append([r, g, b])

print(min(dp_table[-1]))