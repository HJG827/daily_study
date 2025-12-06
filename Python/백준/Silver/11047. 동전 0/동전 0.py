import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
ans = 0
idx = N - 1

while K > 0:
    if K >= coins[idx]:
        ans += (K // coins[idx])
        K %= coins[idx]
    idx -= 1


print(ans)