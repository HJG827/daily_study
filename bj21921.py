# 블로그

import sys
input = sys.stdin.readline

N, X = map(int, input().split())
visitors = list(map(int, input().split()))
ans = 0
cnt = 1

for i in range(X):
    ans += visitors[i]
window = ans

for i in range(N-X):
    window -= visitors[i]
    window += visitors[X+i]

    if window > ans:
        ans = window
        cnt = 1

    elif window == ans:
        cnt += 1

if ans == 0:
    print("SAD")
else:
    print(ans)
    print(cnt)  