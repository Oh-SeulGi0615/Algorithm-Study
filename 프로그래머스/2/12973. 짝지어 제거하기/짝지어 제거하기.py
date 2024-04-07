def solution(s):
    answer = -1

    from collections import deque

    list_ = list(s)

    left = deque([])
    right = deque(list_)

    cnt = 0
    while True:
        if cnt == len(list_):
            break

        if len(left) == 0 or left[-1] != right[0]:
            left.append(right.popleft())
        else:
            left.pop()
            right.popleft()

        cnt += 1

    if len(left) == len(right) == 0:
        answer = 1
    else:
        answer = 0

    return answer