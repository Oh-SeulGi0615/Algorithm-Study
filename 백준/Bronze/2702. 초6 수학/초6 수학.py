import sys
input = sys.stdin.readline

def gcd(num1, num2):
    result = []
    for i in range(1, min(num1, num2)+1):
        if num1 % i == 0 and num2 % i == 0:
            result.append(i)
    return result[-1]

for _ in range(int(input())):
    a, b = map(int, input().split())

    gcd_ = gcd(a, b)
    lcm_ = gcd_ * int(a / gcd_) * int(b / gcd_)
    
    print(lcm_, gcd_)