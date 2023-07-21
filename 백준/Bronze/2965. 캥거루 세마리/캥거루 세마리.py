import sys
input = sys.stdin.readline

arr = list(map(int, input().split()))

arr2 = [arr[i] - arr[i-1] for i in range(1,len(arr))]

print(max(arr2)-1)
