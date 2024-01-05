import sys
input = sys.stdin.readline

arr = {i:[] for i in range(100)}
for i in range(100):
    for j in range(1, 11):
        if (i ** j) % 10 in arr[i]:
            break
        arr[i].append((i ** j) % 10)

for _ in range(int(input())):
    a, b = map(int, input().split())
    
    if arr[a][b % len(arr[a]) - 1] != 0:
        print(arr[a][b % len(arr[a]) - 1])
    else: print(10)