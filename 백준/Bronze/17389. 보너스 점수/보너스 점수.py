import sys
input = sys.stdin.readline

n = int(input())
arr = list(input().rstrip())

score = 0
bonus = 0
if arr[0] == 'O':
    score += 1

for i in range(1, n):
    if arr[i] == 'O' and arr[i-1] == 'O':
        bonus += 1
        score += (i+1) + bonus
    elif arr[i] == 'O' and arr[i-1] != 'O':
        bonus = 0
        score += (i+1) + bonus

print(score)