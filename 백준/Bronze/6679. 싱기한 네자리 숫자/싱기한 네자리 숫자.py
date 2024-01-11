import sys
input = sys.stdin.readline

def check(num, n):
    arr = []
    a, b = divmod(num, n**3)
    arr.append(a)

    c, d = divmod(b, n**2)
    arr.append(c)

    e, f = divmod(d, n)
    arr.append(e)
    arr.append(f)
    
    return sum(arr)

for i in range(1000, 10000):
    if check(i, 10) == check(i, 12) == check(i, 16):
        print(i)