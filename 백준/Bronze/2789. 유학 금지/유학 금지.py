import sys
input = sys.stdin.readline

list_ = ['C','A','M','B','R','I','D','G','E']

string = input().rstrip()
result = ''
for i in  string:
    if i not in list_:
        result += i

print(result)