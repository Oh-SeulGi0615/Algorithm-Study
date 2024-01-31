import sys
input = sys.stdin.readline

from collections import deque

list_ = deque([])
for _ in range(int(input())):
    arr = list(map(int, input().split()))

    if arr[0] == 1:
        list_.appendleft(arr[1])
    elif arr[0] == 2:
        list_.append(arr[1])
    elif arr[0] == 3:
        if len(list_) > 0:
            print(list_.popleft())
        else:
            print(-1)
    elif arr[0] == 4:
        if len(list_) > 0:
            print(list_.pop())
        else:
            print(-1)
    elif arr[0] == 5:
        print(len(list_))
    elif arr[0] == 6:
        if len(list_) == 0:
            print(1)
        else:
            print(0)
    elif arr[0] == 7:
        if len(list_) > 0:
            print(list_[0])
        else:
            print(-1)
    elif arr[0] == 8:
        if len(list_) > 0:
            print(list_[-1])
        else:
            print(-1)