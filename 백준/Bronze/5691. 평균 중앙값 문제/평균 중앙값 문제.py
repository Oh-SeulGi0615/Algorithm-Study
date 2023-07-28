import sys
input = sys.stdin.readline

while True:
    arr = list(map(int, input().split()))
    if arr == [0,0]:
        break

    a = (arr[0] * 3) - arr[0] - arr[1]
    print(a)