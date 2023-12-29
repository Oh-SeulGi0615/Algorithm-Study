import sys
input = sys.stdin.readline

def rev(num):
    arr = list(str(num))[::-1]
    num2 = ''.join(arr)
    return int(num2)

x, y = map(int, input().split())

print(rev(rev(x) + rev(y)))