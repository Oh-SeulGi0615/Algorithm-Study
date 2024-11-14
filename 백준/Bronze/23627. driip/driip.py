char = input().rstrip()

cute = True

if len(char) < len('driip'):
    cute = False
elif char[-5:] != 'driip':
    cute = False

if cute:
    print('cute')
else:
    print('not cute')