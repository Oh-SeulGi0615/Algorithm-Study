import sys
input = sys.stdin.readline

now = list(map(int, input().split(':')))
start = list(map(int, input().split(':')))

hour = start[0] - now[0]
minutes = start[1] - now[1]
seconds = start[2] - now[2]

if seconds < 0:
    minutes -= 1
    seconds += 60
if minutes < 0:
    hour -= 1
    minutes += 60
if hour < 0:
    hour += 24

print(f'{str(hour).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}')