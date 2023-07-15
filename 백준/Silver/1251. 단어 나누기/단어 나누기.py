import sys
input = sys.stdin.readline

a = input().rstrip()

list_ = []
for i in range(1,len(a)-1):
    for j in range(i+1,len(a)):
        b, c, d = a[:i], a[i:j], a[j:]

        result = ''
        result += b[::-1] + c[::-1] + d[::-1]
        list_.append(result)

print(min(list_))