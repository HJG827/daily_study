from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
jump = {}

INF = 10**9

for _ in range(N + M):
    a, b = map(int, input().split())
    jump[a] = b

board = [INF] * 101

q = deque()
q.append(1)
board[1] = 0

while q:
    now = q.popleft()

    for move in range(1, 7):
        next = now + move
        if next < 101:
            to = jump.get(next, next)
            if board[to] > board[now] + 1:
                board[to] = board[now] + 1
                q.append(to)

print(board[100])
