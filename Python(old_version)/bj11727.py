# 2×n 타일링 2

dp = [0] * 1002
dp[1] = 1
dp[2] = 3

N = int(input())

for i in range(3, N+1):
    dp[i] = (dp[i-2] * 2 + dp[i-1]) % 10007

print(dp[N])