import sys, heapq
input = sys.stdin.readline

n = int(input())

triangle = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (i + 1) for i in range(n)]

dp[0][0] = triangle[0][0]

for r in range(1, n):
    for c in range(r + 1):
        if c == 0:
            dp[r][c] = triangle[r][c] + dp[r - 1][c]
        elif c == r:
            dp[r][c] = triangle[r][c] + dp[r - 1][c - 1]
        else:
            dp[r][c] = triangle[r][c] + max(dp[r - 1][c], dp[r - 1][c - 1])

print(max(dp[n - 1]))
