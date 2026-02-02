import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

arr = sorted(arr, key=lambda x: (-x[1], -x[2], -x[3]))

rank = 1
person = 0
state = [0, 0, 0]
dict_ = {(i+1):0 for i in range(n)}
for i in range(n):
  if i == 0:
    person += 1
    state = arr[i][1:]

  elif arr[i][1:] != state:
    rank += person
    person = 1
    state = arr[i][1:]

  else:
    person += 1
  
  dict_[arr[i][0]] = rank
  
print(dict_[k])