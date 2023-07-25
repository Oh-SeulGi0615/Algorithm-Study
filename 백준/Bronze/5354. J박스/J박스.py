import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    a = int(input())

    if a <= 2:
        for i in range(a):
            print('#' * a)
    else:
        for i in range(a):
            if i == 0 or i == (a-1):
                print('#' * a)
            else:
                print('#' + ('J' * (a - 2)) + '#')
    print()