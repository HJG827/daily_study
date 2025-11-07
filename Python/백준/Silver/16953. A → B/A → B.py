A, B = map(int, input().split())
ans = 1

while A < B:
    if B % 10 == 1:
        B //= 10
        ans += 1
    elif B % 2 == 0:
        B //= 2
        ans += 1
    else:
        ans = -1
        break

if A != B:
    ans = -1
print(ans)