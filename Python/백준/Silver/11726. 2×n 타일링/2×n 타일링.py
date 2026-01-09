import sys
input = sys.stdin.readline

n = int(input())


if n < 4:
    print(n)
else:
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        if i < 4:
            dp[i] = i
        else:
            dp[i] = (dp[i - 1] + dp[i - 2]) % 10007
    print(dp[n])