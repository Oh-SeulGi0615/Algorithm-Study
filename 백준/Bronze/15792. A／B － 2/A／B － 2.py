a, b = map(int, input().split())

result = str(a//b) + '.'

i = 0
while a % b != 0 and i < 1000:
    a = (a % b) * 10
    i += 1
    result += str(a//b)

print(result)