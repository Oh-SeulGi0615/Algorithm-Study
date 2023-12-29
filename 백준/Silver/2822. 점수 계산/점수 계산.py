import sys
input = sys.stdin.readline

arr = [int(input()) for _ in range(8)]

arr2 = sorted(arr)[::-1][:5]
arr3 = sorted([arr.index(i)+1 for i in arr2])

print(sum(arr2))
print(*arr3)