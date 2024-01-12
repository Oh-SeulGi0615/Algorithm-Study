import sys
input = sys.stdin.readline

while True:
    n = input().rstrip()
    if n == '0':
        break

    arr = list(map(int, n))
    while len(arr) > 1:
        arr_sum = sum(arr)
        arr = list(map(int, str(arr_sum)))

    print(*arr)