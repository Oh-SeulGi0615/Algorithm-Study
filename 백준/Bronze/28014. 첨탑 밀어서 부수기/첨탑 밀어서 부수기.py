import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

tower = []
tower.append(arr[0])
for i in range(1,n):
    if arr[i] >= arr[i-1]:
        tower.append(arr[i])

print(len(tower))