import sys
input = sys.stdin.readline

n = int(input())
arr1 = [list(map(int, input().split())) for _ in range(n)]
arr2 = [list(map(int, input().split())) for _ in range(n)]

arr1 = sorted(arr1, key=lambda x: (x[0], x[1]))
arr2 = sorted(arr2, key=lambda x: (x[0], x[1]))

print(arr2[0][0] - arr1[0][0], arr2[0][1] - arr1[0][1])