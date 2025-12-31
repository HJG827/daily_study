import sys
input = sys.stdin.readline

T = int(input())

N = [int(input()) for _ in range(T)]
max_N = max(N)

if max_N < 4:
    dp = [1] * 4

else:
    dp = [1] * (max_N + 1)
    for i in range(4, max_N + 1):
        dp[i] = dp[i - 3] + dp[i - 2]
    
for t in range(T):
    print(dp[N[t]])