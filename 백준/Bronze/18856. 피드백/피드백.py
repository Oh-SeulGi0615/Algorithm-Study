import sys
input = sys.stdin.readline

n = int(input())

arr = [i for i in range(1, n)]

def check(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

num = arr[-1] + 1
while True:
    if check(num) == True:
        arr.append(num)
        break
    num += 1

print(n)
print(*arr)