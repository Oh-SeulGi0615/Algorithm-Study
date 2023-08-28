import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

answer = 0
while len(arr) > 2:
    if arr[0] > arr[-1]:
        answer += sum(arr[:-1]) * arr[-1]
        arr.pop()
    else:
        answer += sum(arr[1:]) * arr[0]
        arr.remove(arr[0])

answer += arr[0] * arr[1]
print(answer)