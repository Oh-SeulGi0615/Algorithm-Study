import sys
input = sys.stdin.readline

arr = []
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    arr.append([a, b])

arr = sorted(arr, key=lambda x: x)

end_time = 0
for i in arr:
    start = i[0]
    end = i[1]

    if end_time > start:
        start = end_time
        end_time = start + end
    else:
        end_time = start + end

print(end_time)