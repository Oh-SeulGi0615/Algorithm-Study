import sys
input = sys.stdin.readline

n = int(input())
arr1 = list(map(int, list(input().rstrip())))
arr2 = list(map(int, list(input().rstrip())))

result = [i+j for i, j in zip(arr1, arr2)]

if n % 2 == 1:
    if 0 in result or 2 in result:
        print('Deletion failed')
    else:
        print('Deletion succeeded')
else:
    if 1 in result:
        print('Deletion failed')
    else:
        print('Deletion succeeded')