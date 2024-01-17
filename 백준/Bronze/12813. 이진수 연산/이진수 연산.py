import sys
input = sys.stdin.readline

a = input().rstrip()
b = input().rstrip()

a_ = int(a, 2)
b_ = int(b, 2)

print(str(bin(a_ & b_)[2:]).zfill(100000))
print(str(bin(a_ | b_)[2:]).zfill(100000))
print(str(bin(a_ ^ b_)[2:]).zfill(100000))

result_a = ''.join(['1' if a[i] == '0' else '0' for i in range(len(a))])
result_b = ''.join(['1' if b[i] == '0' else '0' for i in range(len(b))])

print(result_a.zfill(100000))
print(result_b.zfill(100000))