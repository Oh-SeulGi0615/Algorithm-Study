import sys
input = sys.stdin.readline

arr1 = [int(input()) for _ in range(10)]
arr2 = [int(input()) for _ in range(10)]

arr1 = sorted(arr1, key=lambda x: -x)[:3]
arr2 = sorted(arr2, key=lambda x: -x)[:3]

print(sum(arr1), end=' ')
print(sum(arr2))