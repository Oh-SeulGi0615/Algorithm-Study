import sys
input = sys.stdin.readline

from collections import deque

dict_ = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
deq = deque(['Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday'])

d, m = map(int, input().split())

day, month = 1, 1
while True:
    if day == d and month == m:
        break

    day += 1
    deq.rotate(-1)

    if day > dict_[month]:
        month += 1
        day = 1

print(deq[0])