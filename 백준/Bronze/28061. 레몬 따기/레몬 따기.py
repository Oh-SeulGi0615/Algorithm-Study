import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

home = len(arr)
dict_ = {}

for i in range(home):
    dict_[i+1] = arr[i] - (home - i)

answer = sorted(dict_.items(), key=lambda x: -x[1])

print(answer[0][1])