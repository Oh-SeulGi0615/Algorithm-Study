import sys
input = sys.stdin.readline

n, k = map(int, input().split())

def check(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

arr_check = [i for i in range(2, n+1) if check(i) == True]
arr_n = [i for i in range(2, n+1)]

result = []
for i in arr_check:
    for j in arr_n:
        if j % i == 0:
            result.append(j)
            arr_n.remove(j)

print(result[k-1])