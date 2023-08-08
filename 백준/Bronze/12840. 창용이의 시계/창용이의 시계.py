import sys
input = sys.stdin.readline

arr = list(map(int, input().split()))

for _ in range(int(input())):
    arr2 = list(map(int, input().split()))

    if arr2[0] == 3:
        print(*arr)
    else:
        total = arr[0] * 3600 + arr[1] * 60 + arr[2]

        if arr2[0] == 1:
            total += arr2[1]
        elif arr2[0] == 2:
            total -= arr2[1]

        if total < 0:
            total += 86400

        total = total % 86400
        arr[0], c = divmod(total, 3600)
        arr[1], arr[2] = divmod(c, 60)