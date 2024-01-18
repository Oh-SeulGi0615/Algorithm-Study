import sys
input = sys.stdin.readline

string1 = ''.join([i for i in input().rstrip() if i.isalpha()])
string2 = input().rstrip()

if string2 in string1: print(1)
else: print(0)