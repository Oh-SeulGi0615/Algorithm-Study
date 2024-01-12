import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

cnt_l, cnt_r = 1, 1
height_l, height_r = arr[0], arr[-1]
for i in range(1, len(arr)):
    if arr[i] > height_l:
        cnt_l += 1
        height_l = arr[i]

for j in range(len(arr) - 2, -1, -1):
    if arr[j] > height_r:
        cnt_r += 1
        height_r = arr[j]

print(cnt_l, cnt_r, sep='\n')