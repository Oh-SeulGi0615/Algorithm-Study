n = int(input())

arr = [list(input().split()) for _ in range(n)]
arr = sorted(arr, key=lambda x: int(x[1]))

result = ''
for i in arr:
    char = i[0][int(i[2])-1].upper()
    result += char

print(result)