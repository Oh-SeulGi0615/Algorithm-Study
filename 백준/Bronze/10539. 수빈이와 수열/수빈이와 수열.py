import sys
input = sys.stdin.readline

n = int(input())
arr_b = list(map(int, input().split()))

arr_a = [arr_b[0]]
for i in range(1, len(arr_b)):
    component = (arr_b[i] * (i+1)) - sum(arr_a)
    arr_a.append(component)

print(*arr_a)