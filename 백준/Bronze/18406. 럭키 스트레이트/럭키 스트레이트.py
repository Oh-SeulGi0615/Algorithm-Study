import sys
input = sys.stdin.readline

arr = list(map(int, (list(str(input().rstrip())))))
half = int(len(arr) / 2)

if sum(arr[:half]) == sum(arr[half:]):
    print('LUCKY')
else:
    print('READY')