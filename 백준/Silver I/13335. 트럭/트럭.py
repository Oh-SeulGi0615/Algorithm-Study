import sys
input = sys.stdin.readline

from collections import deque

n, w, l = map(int, input().split())
arr = list(map(int, input().split()))[::-1]

bridge = deque(0 for _ in range(w))
cross = []
time = 0

while True:
    if len(cross) == n:
        break

    if len(arr) > 0 and sum(list(bridge)[1:]) + arr[-1] <= l:
        bridge.append(arr[-1])
        a = bridge.popleft()
        arr.pop()
        time += 1
    elif len(arr) == 0 or sum(list(bridge)[1:]) + arr[-1] > l:
        bridge.append(0)
        a = bridge.popleft()
        time += 1

    if a != 0:
        cross.append(a)

print(time)