import sys
input = sys.stdin.readline

for _ in range(int(input())):
    arr = list(set(list(input().rstrip())))

    print(len(arr))