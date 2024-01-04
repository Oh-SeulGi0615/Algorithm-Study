import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
b, c = map(int, input().split())

test_proctor = n
arr2 = list(map(lambda x: x-b, arr))

for i in arr2:
    if i <= 0:
        continue
    share, remainder = divmod(i, c)
    test_proctor += share
    if remainder > 0:
        test_proctor += 1

print(test_proctor)