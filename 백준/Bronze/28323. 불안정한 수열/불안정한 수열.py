import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr2 = []
for i in arr:
    if i % 2 == 0:
        arr2.append(0)
    else:
        arr2.append(1)

for j in range(len(arr)-1):
    if (arr2[j] == 0 and arr2[j+1] == 1) or (arr2[j] == 1 and arr2[j+1] == 0):
        pass
    else:
        arr2[j] = -1

arr3 = list(map(lambda x: x >= 0, arr2))

print(arr3.count(True))