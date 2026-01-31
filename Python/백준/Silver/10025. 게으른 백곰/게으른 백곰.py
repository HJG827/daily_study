import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [0] * 2000001

max_x = 0
for _ in range(N):
    g, x = map(int, input().split())
    arr[x] += g
    if x > max_x:
        max_x = x

ice = sum(arr[:2 * K + 1])
ans = ice

idx = K

while idx < max_x - K:
    idx += 1
    ice -= arr[idx - K - 1]
    ice += arr[idx + K]
    if ice > ans:
        ans = ice


print(ans)