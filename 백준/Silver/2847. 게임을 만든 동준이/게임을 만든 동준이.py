import sys
input = sys.stdin.readline

n = int(input())
if n > 1:
    arr = [int(input()) for _ in range(n)][::-1]
    
    idx = 0
    fix = 0
    while True:
        if idx >= len(arr)-1:
            break
        if arr[idx] <= arr[idx+1]:
            arr[idx+1] -=1
            fix += 1
        else:
            idx += 1
    print(fix)
else:
    print(0)