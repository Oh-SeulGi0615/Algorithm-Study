import sys
input = sys.stdin.readline

arr = list(map(int, input().split()))

def check(arr):
    for i in range(1, len(arr)):
        if arr[i-1] > arr[i]:
            return False
    return True

if check(arr) == True:
    print('Good')
else:
    print('Bad')