import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a = list(input().rstrip())
    b = list(input().rstrip())

    cnt = 0
    for i, j in zip(a, b):
        if i != j:
            cnt += 1
    
    print(f'Hamming distance is {cnt}.')