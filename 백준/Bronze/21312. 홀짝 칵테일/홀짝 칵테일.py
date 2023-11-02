import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
arr = [a, b, c, a*b, a*c, b*c, a*b*c]

odd, even = 0, 0
for num in arr:
    if num % 2 == 0 and num > even:
        even = num
    elif num % 2 != 0 and num > odd:
        odd = num

if odd != 0:
    print(odd)
else:
    print(even)