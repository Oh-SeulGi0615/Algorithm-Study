import sys
input = sys.stdin.readline

arr1 = list(map(int, input().split()))

arr1.sort()

sum1 = arr1[0] + arr1[-1]
sum2 = arr1[1] + arr1[2]

print(max(sum1,sum2) - min(sum1,sum2))