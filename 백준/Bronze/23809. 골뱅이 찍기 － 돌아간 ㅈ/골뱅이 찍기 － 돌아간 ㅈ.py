n = int(input())

strings = ['@   @', '@  @', '@@@', '@  @', '@   @']
result = []

for string in strings:
    a = []
    for char in string:
        a.append(char * n)
    for _ in range(n):
        result.append(''.join(a))

for i in result:
    print(i)