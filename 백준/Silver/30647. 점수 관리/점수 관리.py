import sys
input = sys.stdin.readline

import json
n = int(input())

data = ''
for i in range(n):
  string = input().rstrip()
  data += string

json_data = json.loads(data)
json_data = sorted(json_data, key=lambda x: (-x['score'], x['name']))

scr = 0
rank = 1
person = 0
res = []
for j in range(len(json_data)):
  name = json_data[j]['name']
  score = json_data[j]['score']
  is_hidden = json_data[j]['isHidden']

  if j == 0:
    scr = score
    person += 1
  else:
    if score == scr:
      person += 1
    else:
      scr = score
      rank += person
      person = 1
  
  if is_hidden != 1:
    res.append([rank, name, score])

for case in res:
  print(*case)