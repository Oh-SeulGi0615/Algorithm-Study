import sys
input = sys.stdin.readline

dict_ = {i:2**i for i in range(31)}

for _ in range(int(input())):
    a = int(input())
    if a in dict_.values():
        print(1)
    else:
        print(0)