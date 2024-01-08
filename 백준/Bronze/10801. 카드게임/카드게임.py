import sys
input = sys.stdin.readline

arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))

win_a, win_b, draw = 0, 0, 0
for i in range(len(arr_a)):
    if arr_a[i] > arr_b[i] : win_a += 1
    elif arr_a[i] < arr_b[i] : win_b += 1
    else: draw += 1

if win_a > win_b: print('A')
elif win_b > win_a : print('B')
else: print('D')