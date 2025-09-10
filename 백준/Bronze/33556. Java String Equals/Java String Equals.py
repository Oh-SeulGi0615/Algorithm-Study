string1 = input()
string2 = input()

if string1 == 'null':
    print('NullPointerException')
    print('NullPointerException')
elif string2 == 'null':
    print('false')
    print('false')
else:
    if string1 == string2:
        print('true')
    else:
        print('false')

    if string1.lower() == string2.lower():
        print('true')
    else:
        print('false')