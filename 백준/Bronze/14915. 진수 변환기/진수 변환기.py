m, n = map(int,input().split())

mapping = list('0123456789ABCDEF')
result = []

if m == 0:
    result.append('0')
else:
    while m:
        result.append(mapping[m % n])
        m //= n

print(''.join(result[::-1]))