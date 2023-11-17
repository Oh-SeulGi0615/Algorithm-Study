import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

if 0 in arr:
    if n % 2 == 0:
        if arr.count(0) >= int(len(arr) / 2):
            print('INVALID')
        elif arr.count(1) > arr.count(-1):
            print('APPROVED')
        elif arr.count(1) <= arr.count(-1):
            print('REJECTED')
    else:
        if arr.count(0) > int(len(arr) / 2):
            print('INVALID')
        elif arr.count(1) > arr.count(-1):
            print('APPROVED')
        elif arr.count(1) <= arr.count(-1):
            print('REJECTED')
else:
    if arr.count(1) > arr.count(-1):
        print('APPROVED')
    else:
        print('REJECTED')