import sys
input = sys.stdin.readline

n = int(input())
string = input().rstrip()

status = 'NO'
for i in range(1, n+1):
  cnt = 0
  for j in range(i):
    if string[:i][j] != string[-i:][j]:
      cnt += 1
  
  if cnt == 1:
    status = 'YES'

print(status)