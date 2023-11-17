import sys
input = sys.stdin.readline

n = int(input())
char = input().rstrip().replace('security', '1').replace('bigdata', '2')
arr = list(map(int, char))

security = arr.count(1)
bigdata = arr.count(2)

if security > bigdata:
    print('security!')
elif security < bigdata:
    print('bigdata?')
else:
    print('bigdata? security!')