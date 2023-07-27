import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    a, b = map(int, input().split())

    reward = 0
    if a == 0:
        pass
    elif a == 1:
        reward += 5000000
    elif a <= 3:
        reward += 3000000
    elif a <= 6:
        reward += 2000000
    elif a <= 10:
        reward += 500000
    elif a <= 15:
        reward += 300000
    elif a <= 21:
        reward += 100000

    if b == 0:
        pass
    elif b == 1:
        reward += 5120000
    elif b <= 3:
        reward += 2560000
    elif b <= 7:
        reward += 1280000
    elif b <= 15:
        reward += 640000
    elif b <= 31:
        reward += 320000
    
    print(reward)