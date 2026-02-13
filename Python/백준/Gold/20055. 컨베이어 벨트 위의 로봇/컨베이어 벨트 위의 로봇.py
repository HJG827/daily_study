import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())

belt = deque(list(map(int, input().split())))
robot = deque([0] * (2 * N))

ans = 0
check = 0

while check < K:
    belt.rotate(1)
    robot.rotate(1)
    robot[N - 1] = 0

    for i in range(N - 2, -1, -1):
        if (robot[i]
            and not robot[i + 1]
            and belt[i + 1] > 0):
                robot[i + 1] += 1
                robot[i] -= 1
                belt[i + 1] -= 1

                if belt[i + 1] == 0:
                    check += 1
    
    if belt[0] > 0:
        robot[0] = 1
        belt[0] -= 1

        if belt[0] == 0:
             check += 1

    robot[N - 1] = 0

    ans += 1

print(ans)