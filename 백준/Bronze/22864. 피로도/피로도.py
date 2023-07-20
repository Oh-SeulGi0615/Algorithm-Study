import sys
input = sys.stdin.readline

a, b, c, m = map(int, input().split())

time = 0
task = 0
tired = 0

while True:
    if time == 24:
        break
    if a > m:
        break

    if tired + a <= m:
        tired += a
        task += b
        time += 1
    elif tired + a > m:
        if tired >= c:
            tired -= c
            time += 1
        elif tired < c:
            tired = 0
            time += 1

print(task)