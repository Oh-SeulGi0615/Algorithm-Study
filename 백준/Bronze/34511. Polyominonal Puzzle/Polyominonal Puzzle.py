import sys

n, m = map(int, sys.stdin.readline().split())
board = []
for _ in range(n):
  arr = list(sys.stdin.readline().rstrip())
  arr.append('.')
  board.append(arr)
board.append(['.'] * (m + 1))

cnt = 0
for i in range(n):
  for j in range(m):
    if board[i][j] == 'X':
      if board[i+1][j] == 'Y':
        cnt += 1
      if board[i][j+1] == 'Y':
        cnt += 1

    elif board[i][j] == 'Y':
      if board[i+1][j] == 'X':
        cnt += 1
      if board[i][j+1] == 'X':
        cnt += 1

print(cnt)