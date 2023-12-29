import sys
input = sys.stdin.readline

for _ in range(int(input())):
    arr = list(map(int, input().split()))
    arr.remove(max(arr))
    arr.remove(min(arr))

    if max(arr) - min(arr) >= 4:
        print('KIN')
    else:
        print(sum(arr))