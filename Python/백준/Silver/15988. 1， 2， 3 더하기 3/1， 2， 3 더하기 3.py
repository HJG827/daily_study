import sys
input = sys.stdin.readline

T = int(input())

numbers = []

for _ in range(T):
    N = int(input())
    numbers.append(N)

max_number = max(numbers)
dp = [0] * (max_number + 1)

if max_number >= 1:
    dp[1] = 1
if max_number >= 2:
    dp[2] = 2
if max_number >= 3:
    dp[3] = 4

for i in range(1, max_number - 2):
    dp[i + 3] = (dp[i] + dp[i + 1] + dp[i + 2]) % 1000000009

for number in numbers:
    print(dp[number])