import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]
dp[0][0] = 1

for r in range(N):
    for c in range(N):
        jump = arr[r][c]

        if jump == 0:
            continue
        
        nr = r + jump
        nc = c + jump

        if nr < N:
            dp[nr][c] += dp[r][c]
        if nc < N:
            dp[r][nc] += dp[r][c]

print(dp[N - 1][N - 1])