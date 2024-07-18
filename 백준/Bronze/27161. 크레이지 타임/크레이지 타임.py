from collections import deque

clock = deque([i for i in range(1, 13)])
direction = -1

for _ in range(int(input())):
    s, x = input().split()

    if s != 'HOURGLASS' and int(x) == clock[0]:
        print(clock[0], 'YES')
        clock.rotate(direction)
    elif s == 'HOURGLASS' and int(x) != clock[0]:
        print(clock[0], 'NO')
        direction *= -1
        clock.rotate(direction)
    else:
        print(clock[0], 'NO')
        clock.rotate(direction)