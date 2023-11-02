import sys
input = sys.stdin.readline

n = int(input())

if n % 2 == 0:
    char = 'a'
    print(n * char)
else:
    char1, center, char2 = 'a', 'a', 'a'
    print(char1 * int((n-1)/2) + center + char2 * int((n-1)/2))