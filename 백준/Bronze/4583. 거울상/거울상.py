mirror = {
    'b': 'd',
    'd': 'b',
    'p': 'q',
    'q': 'p',
    'i': 'i',
    'o': 'o',
    'v': 'v',
    'w': 'w',
    'x': 'x'
}

while True:
    list_ = list(input().rstrip())
    if list_[0] == '#':
        break

    reverse = []
    for char in list_:
        if char in mirror.keys():
            reverse.append(mirror[char])
        else:
            reverse.append('INV')
    
    if 'INV' in reverse:
        print('INVALID')
    else:
        print(''.join(reverse[::-1]))