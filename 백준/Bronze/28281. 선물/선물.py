import sys
input = sys.stdin.readline

n, x = map(int, input().split())
arr = list(map(int, input().split()))

arr2 = []
for i in range(len(arr)-1):
    sum = (arr[i] * x) + (arr[i+1] * x)
    arr2.append(sum)

print(min(arr2))