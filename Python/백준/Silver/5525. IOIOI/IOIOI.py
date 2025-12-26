import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input()

P = "I" + N * "OI"
ans = 0

for i in range(M - len(P) + 1):
    if S[i : i + len(P)] == P:
        ans += 1

print(ans)