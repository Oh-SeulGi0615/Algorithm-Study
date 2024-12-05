r, c = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(r)]

parking = [0, 0, 0, 0, 0]
for i in range(r-1):
  for j in range(c-1):
    car = [arr[i][j], arr[i][j+1], arr[i+1][j], arr[i+1][j+1]]
    if '#' in car:
      continue
    if 'X' not in car:
      parking[0] += 1
    elif car.count('X') >= 1:
      parking[car.count('X')] += 1
    
print(*parking, sep='\n')