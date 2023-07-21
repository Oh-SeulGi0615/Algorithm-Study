import sys
input = sys.stdin.readline

arr = []
for _ in range(5):
    arr2 = list(map(int, input().split()))
    arr.append(sum(arr2))

print(arr.index(max(arr))+1, max(arr))