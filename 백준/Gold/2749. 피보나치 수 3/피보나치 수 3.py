import sys
input = sys.stdin.readline

def fibo(num):
    if num == 1:
        return (0, 1, 1)
    
    a, b, c = fibo(num // 2)
    x = (a*b + b*c) % 1000000
    y = (b*b + c*c) % 1000000
    if num % 2 == 0:
        return (y-x, x, y)
    return (x, y, x+y)

n = int(input())
print(fibo(n)[1])