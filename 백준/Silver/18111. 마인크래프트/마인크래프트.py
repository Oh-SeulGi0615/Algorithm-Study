import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())

arr = []
for _ in range(n):
    arr2 = list(map(int, input().split()))
    arr.extend(arr2)

best_time, best_height = 500*500*256, 0
for i in range(max(arr), min(arr)-1, -1):
    time = 0
    height = i
    current_block = b
    
    need_add, need_sub = 0, 0
    for j in arr:
        if height - j > 0:
            need_add += height - j
        elif height - j < 0:
            need_sub += height - j

    if need_add + need_sub > current_block:
        continue

    if need_add + need_sub < 0:
        time += abs(need_sub) * 2 + abs(need_add)
        current_block += need_add - need_sub
    else:
        time += abs(need_sub) * 2 + abs(need_add)
        current_block += need_add - need_sub

    if best_time > time:
        best_time = time
        best_height = height

print(best_time, best_height)