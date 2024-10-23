import decimal

a, b = map(int, input().split())

print(f'{decimal.Decimal(a) / decimal.Decimal(b):.1999f}')