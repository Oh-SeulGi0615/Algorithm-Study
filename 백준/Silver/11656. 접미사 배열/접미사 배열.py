import sys
input = sys.stdin.readline

string = input().rstrip()
list_ = sorted([string[i:] for i in range(len(string))])

for j in list_: print(j)