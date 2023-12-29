import sys
input = sys.stdin.readline

arr = [0]
for i in range(1, 1001):
    arr2 = [i] * i
    arr.extend(arr2)

a, b = map(int, input().split())

print(sum(arr[a:b+1]))