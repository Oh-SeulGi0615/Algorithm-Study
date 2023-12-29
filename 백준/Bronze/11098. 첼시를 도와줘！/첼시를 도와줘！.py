import sys
input = sys.stdin.readline

for _ in range(int(input())):
    best_price = 0
    best_person = ''

    for _ in range(int(input())):
        price, name = map(str, input().split())
        if int(price) > best_price:
            best_price = int(price)
            best_person = name
    
    print(best_person)