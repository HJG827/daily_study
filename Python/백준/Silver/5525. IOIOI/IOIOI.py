import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input()

i = 0
cnt = 0
ans = 0

while i < M - 2:
    if S[i : i + 3] == "IOI":
        cnt += 1
        i += 2

        if cnt >= N:
            ans += 1
    
    else:
        cnt = 0
        i += 1

print(ans)