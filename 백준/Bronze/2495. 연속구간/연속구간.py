import sys
input = sys.stdin.readline

for _ in range(3):
    now, best = 0, 0
    cnt = 1

    arr = list(map(int, list(input().rstrip())))
    for i in range(len(arr)):
        if arr[i] == now:
            cnt += 1
        else:
            now = arr[i]
    
            if cnt > best:
                best = cnt
                cnt = 1
            else:
                cnt = 1

    if cnt > best:
        best = cnt

    if best == 0:
        print(1)
    else:
        print(best)