from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))

balloons = deque([i + 1, numbers[i]] for i in range(N))


while balloons:
    idx, rotation = balloons.popleft()
    if rotation > 0:
        balloons.rotate(-rotation + 1)
    else:
        balloons.rotate(-rotation)
    print(idx, end=" ")