import sys
input = sys.stdin.readline

from collections import deque

n = int(input())
arr = list(map(int, input().split()))

deq = deque([[i, arr[i-1]] for i in range(1, n+1)])

result = []
while len(deq) > 0:
    a = deq.popleft()
    result.append(a[0])

    if a[1] > 0:
        deq.rotate((-1 * a[1]) + 1)
    elif a[1] < 0:
        deq.rotate(-1 * a[1])

print(*result)