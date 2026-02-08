import sys
input = sys.stdin.readline

N, r, c = map(int, input().split())
ans = 0

for k in range(N, 0, -1):
    half = 2 ** (k - 1)
    block = half ** 2

    q = 0
    if r >= half:
        q += 2
        r -= half
    if c >= half:
        q += 1
        c -= half

    ans += q * block

print(ans)