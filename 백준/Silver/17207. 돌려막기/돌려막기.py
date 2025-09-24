diff, time = [], []
name = {0: 'Inseo', 1: 'Junsuk', 2: 'Jungwoo', 3: 'Jinwoo', 4: 'Youngki'}

for _ in range(5):
  arr = list(map(int, input().split()))
  diff.append(arr)
for _ in range(5):
  arr = list(map(int, input().split()))
  time.append(arr)

tasks = [[0 for _ in range(5)] for _ in range(5)]
for i in range(5):
  for j in range(5):
    task = 0

    for k in range(5):
      task += diff[i][k] * time[k][j]
    
    tasks[i][j] = task

tasks = [sum(tasks[i]) for i in range(5)]

if tasks.count(min(tasks)) == 1:
  print(name[tasks.index(min(tasks))])
else:
  print(name[4-tasks[::-1].index(min(tasks))])