import sys
input = sys.stdin.readline

for _ in range(int(input())):
    k = int(input())

    passenger = 0
    for _ in range(k):
        passenger = int((passenger + 0.5) * 2)

    print(passenger)