n, string = map(str, input().split())
n = int(n)

result = {1:'', 2:'', 3:''}
if n == 1:
    result[1] = string
    result[3] = string[0].upper() + string[1:]
    for i in string:
        if i.isupper():
            result[2] += '_'
            result[2] += i.lower()
        else:
            result[2] += i

elif n == 2:
    result[2] = string
    string_list = string.split('_')
    for component in string_list:
        result[1] += component.capitalize()
        result[3] += component.capitalize()
    result[1] = result[1][0].lower() + result[1][1:]

else:
    result[3] = string
    result[1] = string[0].lower() + string[1:]
    for i in result[1]:
        if i.isupper():
            result[2] += '_'
            result[2] += i.lower()
        else:
            result[2] += i

print(*list(result.values()), sep='\n')