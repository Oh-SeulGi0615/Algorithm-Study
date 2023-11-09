import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int, input().split())))

left, right = 0, len(arr)-1
min_diff = float('inf')
result = (arr[left], arr[right])

while left < right:
    sum_ = arr[left] + arr[right]
    diff = abs(sum_)

    if diff < min_diff:
        min_diff = diff
        result = (arr[left], arr[right])
    
    if sum_ < 0:
        left += 1
    else:
        right -= 1

print(*result)