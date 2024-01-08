import sys
input = sys.stdin.readline

arr = [0, 1, 2, 4]

def dp(num):
    arr.append(arr[num-1] + arr[num-2] + arr[num-3])
    return arr[-1]

for i in range(4, 12):
    dp(i)

for _ in range(int(input())):
    n = int(input())
    print(arr[n])