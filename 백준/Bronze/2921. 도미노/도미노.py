import sys
input = sys.stdin.readline

n = int(input())

arr = []
for i in range(n+1):
    for j in range(i+1):
        arr.append([i, j])

sum_ = 0
for x in range(len(arr)):
    sum_ += sum(arr[x])

print(sum_)