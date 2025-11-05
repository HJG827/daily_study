N = int(input())

dp = [0] * (N + 1)

dp[0] = 1
dp[1] = 3
# dp[2] = 7
# dp[3] = 17
# dp[4] = 41

for i in range(N-1):
    dp[i+2] = (dp[i] + dp[i+1]*2 ) % 9901

print(dp[N])