import sys

n = int(sys.stdin.readline())

dict_ = {}

correct, total = 0, 0
for _ in range(n):
  list_ = sys.stdin.readline().split()
  if list_[1] == 'megalusion':
    continue
  elif list_[1] not in dict_:
    dict_[list_[1]] = [list_[2]]
  elif '4' not in dict_[list_[1]]:
    dict_[list_[1]].append(list_[2])

for i in list(dict_.keys()):
  if '4' in dict_[i]:
    total += len(dict_[i])
    correct += dict_[i].count('4')

if total == 0:
  print(0)
else:
  print((correct / total) * 100)