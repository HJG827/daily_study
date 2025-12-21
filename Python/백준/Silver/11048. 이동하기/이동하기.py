import sys
input = sys.stdin.readline

N, M = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * M for _ in range(N)]

for r in range(N):
    for c in range(M):
        top = 0
        left = 0
        diag = 0

        if r - 1 >= 0:
            top = dp[r - 1][c]
        if c - 1 >= 0:
            left = dp[r][c - 1]
        if r - 1 >= 0 and c - 1 >= 0:
            diag = dp[r - 1][c - 1]

        dp[r][c] = maze[r][c] + max(top, left, diag)

print(dp[N - 1][M - 1])