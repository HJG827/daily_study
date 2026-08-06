import sys, math
input = sys.stdin.readline

n = int(input())
dp = [0] * (n + 1)

squares = []
j = 1
while j ** 2 <= n:
    squares.append(j ** 2)
    j += 1

for i in range(1, n + 1):
    dp[i] = i
    for j in squares:
        if j > i:
            break
        number = dp[i - j] + 1

        if number < dp[i]:
            dp[i] = number
            if dp[i] == 1:
                break

print(dp[n])