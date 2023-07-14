import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

answer = ['+']
stack = [1]
n = 2
loc = 0
while loc < len(arr):
    if len(stack) == 0:
        stack.append(n)
        answer.append('+')
        n += 1
    if stack[-1] < arr[loc]:
        stack.append(n)
        answer.append('+')
        n += 1
    elif stack[-1] > arr[loc]:
        answer.append('NO')
        break
    else:
        stack.pop()
        answer.append('-')
        loc += 1

if 'NO' in answer:
    print('NO')
else:
    for i in answer:
        print(i)