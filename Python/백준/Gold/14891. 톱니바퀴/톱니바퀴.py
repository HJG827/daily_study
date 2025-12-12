from collections import deque
import sys
input = sys.stdin.readline

gears = [0]
gears += [deque(input().strip()) for _ in range(4)]

K = int(input())

for _ in range(K):
    number, direction = map(int, input().split())
    rotate = [0] * 5
    rotate[number] = direction

    for i in range(number - 1, 0, -1):
        if gears[i][2] != gears[i + 1][6]:
            rotate[i] = -rotate[i + 1]
        else:
            break        

    for j in range(number + 1, 5):
        if gears[j - 1][2] != gears[j][6]:
            rotate[j] = -rotate[j - 1]
        else:
            break

    for r in range(1, 5):
        if rotate[r] == 1:
            gears[r].rotate(1)
        elif rotate[r] == -1:
            gears[r].rotate(-1)

ans = 0

for i in range(1, 5):
    if gears[i][0] == '1':
        ans += 2 ** (i - 1)

print(ans)