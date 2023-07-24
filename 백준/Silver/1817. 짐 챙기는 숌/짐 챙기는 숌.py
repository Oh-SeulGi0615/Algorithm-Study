import sys
input = sys.stdin.readline

n, m = map(int, input().split())
if n == 0:
    print(0)
else:
    arr = list(map(int, input().split()))

    box = 0
    total = 0
    for i in range(n):
        if arr[i] > m:
            pass
        else:
            if total + arr[i] > m:
                total = arr[i]
                box += 1
            else:
                total += arr[i]

    if total == 0:
        print(box)
    else:
        print(box + 1)