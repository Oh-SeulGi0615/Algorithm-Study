import sys
input = sys.stdin.readline

correct = [((i-1) % 5)+1 for i in range(1, 11)]
for i in range(1, int(input())+1):
    arr = list(map(int, input().split()))

    if arr == correct:
        print(i)