n = int(input())
a, b = map(int, input().split())

result = ''
result = ('1' * ((a - max((a+b)-n, 0) + (b - max((a+b)-n, 0))))) + ('0' * abs((a+b)-n))

print(int(result, 2))