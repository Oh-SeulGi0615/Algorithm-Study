import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a, b = input().split()

    print('Distances:', end=' ')
    for i in range(len(a)):
        distance = ord(b[i]) - ord(a[i])
        if distance < 0:
            distance += 26
        print(f'{distance}', end=' ')
    print()