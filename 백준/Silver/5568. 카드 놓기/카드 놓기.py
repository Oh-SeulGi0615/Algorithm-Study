import sys
input = sys.stdin.readline

from itertools import permutations

n = int(input())
k = int(input())

arr = [int(input()) for _ in range(n)]

permu = list(permutations(arr, k))
result = set([int(''.join(list(map(str, i)))) for i in permu])

print(len(result))