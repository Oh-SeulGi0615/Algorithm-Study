c, b = map(int, input().split())

result = round(c / b, 10)

if result == int(result):
    print(int(result))
else:
    print(result)