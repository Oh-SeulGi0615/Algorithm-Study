import sys
input = sys.stdin.readline

import math

cnt = 1
while True:
    arr = list(map(int, input().split()))
    if arr == [0]:
        break

    r, w, l = arr[0], arr[1], arr[2]
    dgnl = math.sqrt((w**2) + (l**2))

    if dgnl <= r * 2:
        print(f'Pizza {cnt} fits on the table.')
    else:
        print(f'Pizza {cnt} does not fit on the table.')
    
    cnt += 1