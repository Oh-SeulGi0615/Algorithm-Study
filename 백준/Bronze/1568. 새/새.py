import sys
input = sys.stdin.readline

n = int(input())

bird = n
second, k = 0, 1
while bird > 0:
    if bird >= k:
        bird -= k
        second += 1
        k += 1
    
    else:
        k = 1

        bird -= k
        second += 1
        k += 1

print(second)