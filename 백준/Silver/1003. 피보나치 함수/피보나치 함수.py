fibonacci = {0:[1, 0], 1:[0, 1]}
for i in range(2, 41):
  fibonacci[i] = [(fibonacci[i-1][0] + fibonacci[i-2][0]), fibonacci[i-1][1] + fibonacci[i-2][1]]

for _ in range(int(input())):
  print(*fibonacci[int(input())])