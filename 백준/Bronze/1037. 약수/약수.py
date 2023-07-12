import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

answer = arr[0] * arr[-1]
print(answer)