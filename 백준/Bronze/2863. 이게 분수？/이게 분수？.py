import sys
input = sys.stdin.readline

a, b = map(int, input().split())
c, d = map(int, input().split())

arr = []

result1 = (a/c) + (b/d)
result2 = (c/d) + (a/b)
result3 = (d/b) + (c/a)
result4 = (b/a) + (d/c)

arr.append(result1)
arr.append(result2)
arr.append(result3)
arr.append(result4)

for i in range(len(arr)):
    if arr[i] == max(arr):
        print(i)