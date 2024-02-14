import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
nge = [-1] * len(arr)

stack = []

for i in range(len(arr)):
    if len(stack) == 0 or (stack[-1][0] >= arr[i]):
        stack.append([arr[i], i])
    
    elif stack[-1][0] < arr[i]:
        while stack[-1][0] < arr[i]:
            nge[stack[-1][1]] = arr[i]
            stack.pop()
            if len(stack) == 0:
                break
        stack.append([arr[i], i])

print(*nge)