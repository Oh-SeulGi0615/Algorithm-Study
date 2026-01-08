import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  box = []

  blank = input()
  r, c = map(int, input().split())
  for _ in range(r):
    arr = list(input().rstrip())
    box.append(arr)
  
  candy = 0
  for i in range(r):
    for j in range(c-2):
      if box[i][j] == '>' and box[i][j+1] == 'o' and box[i][j+2] == '<':
        candy += 1
  
  for m in range(r-2):
    for n in range(c):
      if box[m][n] == 'v' and box[m+1][n] == 'o' and box[m+2][n] == '^':
        candy += 1
  
  print(candy)