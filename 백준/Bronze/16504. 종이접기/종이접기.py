import sys
input = sys.stdin.readline

sum_ = 0
for _ in range(int(input())):
    arr = list(map(int, input().split()))
    sum_ += sum(arr)

print(sum_)