n = int(input())
recipe = set(input().split())
my_items = set(input().split())

print(*(recipe - my_items))