import sys
input = sys.stdin.readline

S = input().strip()

zero = 0
one = 0

prev = S[0]

if prev == '0':
    zero = 1
else:
    one = 1

for i in range(1, len(S)):
    now = S[i]
    if prev != now:
        if now == "1":
            one += 1
        elif now == "0":
            zero += 1

    prev = S[i]

print(min(zero, one))