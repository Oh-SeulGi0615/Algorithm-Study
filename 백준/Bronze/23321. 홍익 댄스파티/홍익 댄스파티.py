import sys
input = sys.stdin.readline

string_ = [list(input().rstrip()) for _ in range(5)]
arr = []
for j in range(len(string_[0])):
  res = ''
  for i in range(5):
    res += string_[i][j]
  arr.append(res)

for i in range(len(arr)):
  if arr[i] == '.omln':
    arr[i] = 'owln.'
  elif arr[i] == 'owln.':
    arr[i] = '.omln'

arr2 = []
for j in range(len(arr[0])):
  res = ''
  for i in range(len(arr)):
    res += arr[i][j]
  arr2.append(res)

for char in arr2:
  print(char)