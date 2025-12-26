N = int(input())

if N < 4:
    dp = [0] * 4
else:
    dp = [0] * (N + 1)

dp[1] = 1
dp[2] = 2
dp[3] = 3

if N < 4:
    print(dp[N])
else:
    for i in range(4, N + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 15746

    print(dp[N])