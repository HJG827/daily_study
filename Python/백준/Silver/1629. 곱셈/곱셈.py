import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

def mod_pow(a, b, m):
    if b == 0:
        return 1
    if b == 1:
        return a % m
    half = mod_pow(a, b // 2, m)
    half = (half * half) % m
    if b % 2 == 0:
        return half
    else:
        return (half * (a % m)) % m
    
print(mod_pow(A, B, C))