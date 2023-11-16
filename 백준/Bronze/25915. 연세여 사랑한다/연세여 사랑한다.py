import sys
input = sys.stdin.readline

list_ = list('ILOVEYONSEI')
char = input().rstrip()

arr = [ord(char)]
arr.extend(list(map(lambda x: ord(x), list_)))

result = [abs(arr[i] - arr[i-1]) for i in range(1, len(arr))]

print(sum(result))