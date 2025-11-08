import sys

n, t, p = map(int, sys.stdin.readline().split())
if n != 0:
    arr = list(map(int, sys.stdin.readline().split()))
    arr.append(t)
    arr = sorted(arr, key=lambda x: -x)

    rank = 0
    stack = 0
    cnt = 0
    now = None

    result = 0
    for score in arr:
        if score != now:
            rank += 1
            rank += stack
            stack = 0
            now = score
            cnt += 1
        else:
            stack += 1
            cnt += 1

        if now == t and cnt > p:
            result = -1
        elif now == t:
            result = rank
        
    print(result)

else:
    print(1)