c, b = map(int, input().split())

result = round(max(c, b) / min(c, b), 10)
print(result)