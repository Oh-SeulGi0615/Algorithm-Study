import sys
input = sys.stdin.readline

arr1, arr2 = [], []
for _ in range(4):
    n = int(input())
    arr1.append(n)

for _ in range(2):
    m = int(input())
    arr2.append(m)

arr1.sort()
arr2.sort()

sum = sum(arr1) - arr1[0] + arr2[-1]
print(sum)