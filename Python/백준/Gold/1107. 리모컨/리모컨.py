import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
if M > 0:
    broken = list(map(int, input().split()))
else:
    broken = []

ans = abs(N - 100)

for i in range(1000000):
    press = True

    for ch in str(i):
        if int(ch) in broken:
            press = False
            break

    if press:
        cnt = len(str(i)) + abs(N - i)
        ans = min(cnt, ans)

print(ans)