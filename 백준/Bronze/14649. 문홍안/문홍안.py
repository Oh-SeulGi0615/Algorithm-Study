import sys
input = sys.stdin.readline

p = int(input())
n = int(input())

stone = ['b' for _ in range(100)]
for _ in range(n):
  loc, direct = map(str, input().split())

  if direct == 'R':
    for i in range(int(loc), 100):
      if stone[i] == 'b':
        stone[i] = 'r'
      elif stone[i] == 'r':
        stone[i] = 'g'
      else:
        stone[i] = 'b'
  
  elif direct == 'L':
    for j in range(int(loc)-2, -1, -1):
      if stone[j] == 'b':
        stone[j] = 'r'
      elif stone[j] == 'r':
        stone[j] = 'g'
      else:
        stone[j] = 'b'

r, g, b = stone.count('r'), stone.count('g'), stone.count('b')

print(f'{p * b / (r+g+b):.2f}')
print(f'{p * r / (r+g+b):.2f}')
print(f'{p * g / (r+g+b):.2f}')