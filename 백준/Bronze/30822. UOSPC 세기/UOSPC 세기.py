n = int(input())
string = list(input())

uospc = {'u':0, 'o':0, 's':0, 'p':0, 'c':0}

result = 99
if all(char in string for char in list(uospc.keys())):
    for char in list(uospc.keys()):
        cnt = string.count(char)
        uospc[char] = cnt

print(min(list(uospc.values())))