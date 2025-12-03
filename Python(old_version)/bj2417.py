# 정수 제곱근

import math

N = int(input())
num = math.isqrt(N)

if num*num != N:
    num += 1

print(num)