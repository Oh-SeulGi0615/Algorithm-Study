import sys
input = sys.stdin.readline

from collections import deque

n = int(input())
arr = deque(list(input().rstrip()))

while True:
    if arr.count('s') == arr.count('t'):
        print(''.join(arr))
        break
    arr.popleft()