import sys
input = sys.stdin.readline

from collections import deque

n, m = map(int, input().split())
arr = list(map(int, input().split()))

deq = deque([i for i in range(1, n+1)])

cnt = 0
while len(arr) > 0:
    right = deq.index(arr[0])
    left = len(deq) - deq.index(arr[0])

    if arr[0] == deq[0]:
        arr.pop(0)
        deq.popleft()
    elif right <= left:
        deq.rotate(-1 * right)
        cnt += right
    elif right > left:
        deq.rotate(left)
        cnt += left

print(cnt)