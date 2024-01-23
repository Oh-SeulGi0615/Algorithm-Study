import sys
input = sys.stdin.readline

arr = [int(input()) for _ in range(int(input()))]
arr.sort(reverse=True)

r = []
for i in range(0, len(arr), 3):
    r.append(arr[i:i+3])

score = 0
for j in r:
    if len(j) > 2:
        score += sum(j) - min(j)
    else:
        score += sum(j)

print(score)