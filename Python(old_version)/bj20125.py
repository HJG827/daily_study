# 쿠키의 신체 측정
import sys
input = sys.stdin.readline

N = int(input())
tray = [list(input().strip()) for _ in range(N)]
check = False

for r1 in range(N):
    for c1 in range(N):
        if tray[r1][c1] == '*':
            heart_r = r1 + 1
            heart_c = c1
            check = True
            break
    if check:
        break

heart = False
left_arm = 0
right_arm = 0
for c2 in range(N):
    if c2 == heart_c:
        heart = True

    elif tray[heart_r][c2] == '*':
        if heart:
            right_arm += 1
        else:
            left_arm += 1
    else:
        if heart:
            break

waist = 0
for r2 in range(heart_r+1, N):
    if tray[r2][heart_c] == '*':
        waist += 1
    else:
        break

left_leg = 0
right_leg = 0

for r3 in range(heart_r + waist + 1, N):
    if tray[r3][heart_c - 1] == "*":
        left_leg += 1
    else:
        break

for r4 in range(heart_r + waist + 1, N):
    if tray[r4][heart_c + 1] == "*":
        right_leg += 1
    else:
        break

print(heart_r + 1, heart_c + 1)
print(left_arm, right_arm, waist, left_leg, right_leg)
