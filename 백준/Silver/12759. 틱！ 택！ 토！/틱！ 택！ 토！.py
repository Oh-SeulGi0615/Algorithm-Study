import sys
input = sys.stdin.readline

p = int(input())
arr = [[0] * 3 for _ in range(3)]

turn = p
winner = 0
for _ in range(9):
  i, j = map(int, input().split())

  if turn == 1:
    arr[i-1][j-1] = 1
    turn = 2
  else:
    arr[i-1][j-1] = 2
    turn = 1

  if arr[0][0] == arr[0][1] == arr[0][2] != 0:
    winner = arr[0][0]
    break
  elif arr[1][0] == arr[1][1] == arr[1][2] != 0:
    winner = arr[1][0]
    break
  elif arr[2][0] == arr[2][1] == arr[2][2] != 0:
    winner = arr[2][0]
    break
  elif arr[0][0] == arr[1][0] == arr[2][0] != 0:
    winner = arr[0][0]
    break
  elif arr[0][1] == arr[1][1] == arr[2][1] != 0:
    winner = arr[0][1]
    break
  elif arr[0][2] == arr[1][2] == arr[2][2] != 0:
    winner = arr[0][2]
    break
  elif arr[0][0] == arr[1][1] == arr[2][2] != 0:
    winner = arr[0][0]
    break
  elif arr[0][2] == arr[1][1] == arr[2][0] != 0:
    winner = arr[0][2]
    break

print(winner)