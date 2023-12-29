import sys
input = sys.stdin.readline

from itertools import combinations

arr = [int(input()) for _ in range(9)]

arr2 = list(combinations(arr, 7))

for i in arr2:
    if sum(i) == 100:
        arr3 = sorted(list(i))
        for j in arr3:
            print(j)
        break