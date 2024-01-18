import sys
input = sys.stdin.readline

dict_ = {'-':0, '\\':1, '(':2, '@':3, '?':4, '>':5, '&':6, '%':7, '/':-1}

while True:
    string = input().rstrip()
    if string == '#':
        break

    string_list = string[::-1]

    result = 0
    for i in range(len(string_list)):
        result += dict_[string_list[i]] * (8 ** i)
    
    print(result)