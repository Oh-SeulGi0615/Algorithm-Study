arr = [input() for i in range(2*(int(input()))-1)]

result = eval(''.join(arr).replace('/', '//'))
print(result)