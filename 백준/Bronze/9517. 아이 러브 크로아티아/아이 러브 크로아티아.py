import sys
input = sys.stdin.readline

k = int(input())

time = 0
bomb = k
for _ in range(int(input())):
    t, z = input().split()

    time += int(t)

    if time >= 210:
        print(bomb)
        break

    else:
        if z == 'T':
            if bomb == 8:
                bomb = 1
            else:
                bomb += 1