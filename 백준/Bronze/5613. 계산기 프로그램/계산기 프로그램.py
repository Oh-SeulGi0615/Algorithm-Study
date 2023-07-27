import sys
input = sys.stdin.readline

arr, symbol = [], []
while True:
    a = input().rstrip()
    if a == '=':
        break

    if a.isdigit() == True:
        arr.append(int(a))
    elif a.isdigit() == False:
        symbol.append(a)

result = arr[0]
for i in range(len(symbol)):
    if symbol[i] == '+':
        result += arr[i+1]
    elif symbol[i] == '-':
        result -= arr[i+1]
    elif symbol[i] == '*':
        result = result * arr[i+1]
    elif symbol[i] == '/':
        result = int(result / arr[i+1])

print(result)