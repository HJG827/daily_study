

from collections import deque
import sys
input = sys.stdin.readline

def check_tomatos(arr):
    for r in range(N):
        for c in range(M):
            if arr[r][c] == 0:
                return 1
    return 0


def bfs(arr):
    cnt = 0

    for r in range(N):
        for c in range(M):
            if arr[r][c] == 1:
                q.append([r, c])
    
    while q:
        day = len(q)

        for _ in range(day):
            tr, tc = q.popleft()

            for dr, dc in ([0, 1], [1, 0], [0, -1], [-1, 0]):
                nr = tr + dr
                nc = tc + dc
                if (
                    0 <= nr < N
                    and 0 <= nc < M
                    and arr[nr][nc] == 0
                ):
                    arr[nr][nc] = arr[tr][tc] + 1
                    q.append([nr, nc])
                    cnt = arr[nr][nc]

    return cnt - 1, arr

M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]

q = deque()

result = 0
if check_tomatos(tomato):
    max_day, box = bfs(tomato)
    if check_tomatos(box):
        result = -1
    else:
        result = max_day
    
print(result)
