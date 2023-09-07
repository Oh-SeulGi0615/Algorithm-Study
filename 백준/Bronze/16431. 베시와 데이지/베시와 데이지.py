import sys
input = sys.stdin.readline

bessie = list(map(int, input().split()))
daisy = list(map(int, input().split()))
john = list(map(int, input().split()))

time_daisy = abs(daisy[0] - john[0]) + abs(daisy[1] - john[1])

john_to_bessie = [abs(bessie[0] - john[0]), abs(bessie[1] - john[1])]
time_bessie = 0
while True:
    if john_to_bessie[0] == 0 or john_to_bessie[1] == 0:
        break
    john_to_bessie[0] -= 1
    john_to_bessie[1] -= 1
    time_bessie += 1
time_bessie += john_to_bessie[0] + john_to_bessie[1]

if time_bessie < time_daisy:
    print('bessie')
elif time_bessie > time_daisy:
    print('daisy')
else:
    print('tie')