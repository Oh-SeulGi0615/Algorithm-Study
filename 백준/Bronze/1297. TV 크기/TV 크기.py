import sys
input = sys.stdin.readline

import math

d, h, w = map(int, input().split())

d_ = math.sqrt(h**2 + w**2)
ratio = d / d_

print(math.trunc(h * ratio), math.trunc(w * ratio))