import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    arr = list(map(int, input().split()))

    arr2 = []
    for i in arr:
        if i % 2 == 0:
            arr2.append(i)

    print(sum(arr2), min(arr2))