seats = [['.' for _ in range(20)] for _ in range(10)]

n = int(input())
for _ in range(n):
    seat = input().rstrip()

    row = ord(seat[0]) - 65
    col = int(seat[1:]) - 1

    seats[row][col] = 'o'

for i in range(len(seats)):
    print(*seats[i], sep='')