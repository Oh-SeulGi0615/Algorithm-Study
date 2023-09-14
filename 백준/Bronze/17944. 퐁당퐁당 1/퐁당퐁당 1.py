import sys
input = sys.stdin.readline

n, t = map(int, input().split())

direction = 0
cnt = 1
number = 1
while True:
    if cnt == t:
        break
    if direction == 0:
        number += 1
        cnt += 1
        if number == 2*n:
            direction = 1
    else:
        number -= 1
        cnt += 1
        if number == 1:
            direction = 0

print(number)