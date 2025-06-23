n = int(input())
string = input().rstrip().replace('.','/').replace('|','/').replace(':','/').replace('#','/')

arr = list(map(int, string.split('/')))
print(sum(arr))