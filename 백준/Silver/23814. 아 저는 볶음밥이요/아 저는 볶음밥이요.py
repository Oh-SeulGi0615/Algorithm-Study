import sys

d = int(sys.stdin.readline())
n, m, k = map(int, sys.stdin.readline().split())

max_gmd = (n + m + k) // d

now_gmd = (n // d) + (m // d) + (k // d)

while True:
    if ((n // d) + (m // d) + (k // d)) == max_gmd:
        break

    if n % d > m % d:
        k -= d - (n % d)
        n += d - (n % d)
    else:
        k -= d - (m % d)
        m += d - (m % d)
        
print(k)