X = int(input())
ans = 0

while X > 0:
    if X & 1:
        ans += 1
    X >>= 1

print(ans)