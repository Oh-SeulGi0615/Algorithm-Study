import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
arr = arr[::-1]

day = 1 + len(arr)
def func(arr=list):
    num = len(arr)
    for i in range(num):
        arr[i] -= (num - 1) - i
    return arr

arr2 = func(arr)
print(day + max(arr2))