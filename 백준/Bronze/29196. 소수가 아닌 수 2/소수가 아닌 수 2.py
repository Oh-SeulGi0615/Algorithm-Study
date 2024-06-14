k = float(input())
n = int(k)

for i in range(1, 10):
    if (((k - n) * (10**i)) - int((k - n) * (10**i))) == 0.0:
        p = int((k - n) * (10**i))
        q = 10**i
        break

if (p + (q * n)) > 10**9:
    print('NO')
else:
    print('YES')
    print((p + (q * n)), q)